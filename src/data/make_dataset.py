
import pandas as pd

def load_and_preprocess_data(data_path):
    
    # Import the data from 'credit.csv'
    df = pd.read_csv(data_path)

    # Impute all missing values in all the features
    # Impute all missing values in all the features
    df.fillna({
        'Gender': 'Male',
        'Married': df['Married'].mode()[0],
        'Dependents': df['Dependents'].mode()[0],
        'Education': df['Education'].mode()[0],
        'Self_Employed': df['Self_Employed'].mode()[0],
        'ApplicantIncome': df['ApplicantIncome'].median(),
        'CoapplicantIncome': df['CoapplicantIncome'].median(),
        'LoanAmount': df['LoanAmount'].median(),
        'Loan_Amount_Term': df['Loan_Amount_Term'].mode()[0],
        'Credit_History': df['Credit_History'].mode()[0],
        'Property_Area': df['Property_Area'].mode()[0]
    }, inplace=True)

    # Drop 'Loan_ID' variable from the data
    df = df.drop('Loan_ID', axis=1)

    return df
