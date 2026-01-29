import pytest
import pandas as pd
import numpy as np
import os
import sys
from unittest.mock import MagicMock, patch

# Add src to sys.path to ensure we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.data.make_dataset import load_and_preprocess_data
from src.models.train_model import train_RFmodel
from src.models.predict_model import evaluate_model

# Mock data for testing
@pytest.fixture
def mock_csv_data(tmp_path):
    df = pd.DataFrame({
        'Loan_ID': ['LP001', 'LP002', 'LP003'],
        'Gender': [np.nan, 'Female', 'Male'],
        'Married': ['Yes', np.nan, 'No'],
        'Dependents': ['0', '1', np.nan],
        'Education': ['Graduate', 'Not Graduate', np.nan],
        'Self_Employed': ['No', 'Yes', np.nan],
        'ApplicantIncome': [5000, np.nan, 3000],
        'CoapplicantIncome': [0, 2000, np.nan],
        'LoanAmount': [150, 120, np.nan],
        'Loan_Amount_Term': [360, 360, np.nan],
        'Credit_History': [1.0, 0.0, np.nan],
        'Property_Area': ['Urban', 'Rural', np.nan],
        'Loan_Status': ['Y', 'N', 'Y'] # Target variable mostly likely needed for some cases, though load_and_preprocess_data doesn't use it explicitly for imputation logic shown
    })
    file_path = tmp_path / "credit.csv"
    df.to_csv(file_path, index=False)
    return str(file_path)

def test_load_and_preprocess_data(mock_csv_data):
    """Test data loading and missing value imputation."""
    df = load_and_preprocess_data(mock_csv_data)
    
    # Check if Loan_ID is dropped
    assert 'Loan_ID' not in df.columns
    
    # Check if missing values are filled
    assert df.isnull().sum().sum() == 0
    
    # Specific checks based on the logic in make_dataset.py
    # Gender fills with 'Male'
    assert df['Gender'].iloc[0] == 'Male' 
    # ApplicantIncome fills with median (5000, 3000) -> 4000
    assert df['ApplicantIncome'].iloc[1] == 4000.0

def test_train_RFmodel():
    """Test model training pipeline."""
    # Create synthetic data
    X = pd.DataFrame(np.random.rand(100, 5), columns=[f'f{i}' for i in range(5)])
    y = pd.Series(np.random.randint(0, 2, 100))
    
    # Mock pickle dump to avoid writing file
    with patch('pickle.dump') as mock_dump, \
         patch('builtins.open', new_callable=MagicMock):
        
        model, X_test_scaled, y_test = train_RFmodel(X, y)
        
        # Check outputs
        assert model is not None
        assert len(X_test_scaled) == 20 # 20% of 100
        assert len(y_test) == 20
        
        # Check if model was "saved"
        assert mock_dump.called

def test_evaluate_model():
    """Test evaluation metrics."""
    # Mock model
    class MockModel:
        def predict(self, X):
            return np.array([1, 0, 1])
            
    model = MockModel()
    X_test = np.array([[0.1], [0.2], [0.3]])
    y_test = np.array([1, 0, 0]) # 2/3 correct
    
    accuracy, confusion_mat = evaluate_model(model, X_test, y_test)
    
    assert accuracy == 2/3
    assert confusion_mat.shape == (2, 2)
