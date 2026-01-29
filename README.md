# credit_eligibility_application
This app has been built using Streamlit and deployed with Streamlit community cloud

[Visit the app here](https://loan-application-app.streamlit.app/)

password - streamlit

This application predicts whether someone is eligible for a loan based on inputs derived from the German Credit Risk dataset. The model aims to help users assess loan eligibility by leveraging machine learning predictions.

## Features
- User-friendly interface powered by Streamlit.
- Input form to enter details such as credit history, loan amount, income, and other relevant factors.
- Real-time prediction of loan eligibility based on the trained model.
- Accessible via Streamlit Community Cloud.

## Dataset
The application is trained on the **German Credit Risk dataset**, a widely used dataset for evaluating creditworthiness. It includes features like:
- Age
- Job
- Housing status
- Credit amount
- Duration of credit
- Purpose of loan
- And other factors influencing credit risk.

## Technologies Used
- **Streamlit**: For building the web application.
- **Scikit-learn**: For model training and evaluation.
- **Pandas** and **NumPy**: For data preprocessing and manipulation.
- **Matplotlib** and **Seaborn**: For exploratory data analysis and visualization (if applicable).

## Model
The predictive model is trained using the German Credit Risk dataset. It applies preprocessing steps like encoding categorical variables and scaling numerical features. The classification model used may include algorithms such as Logistic Regression, Random Forest, or XGBoost.

## Future Enhancements
* Adding support for multiple datasets.
* Incorporating explainability tools like SHAP to provide insights into predictions.
* Adding visualizations to better represent user input and model predictions.

## Installation (for local deployment)
If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/credit_eligibility_application.git
   cd credit_eligibility_application

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   ```bash
   streamlit run streamlit.py


 ## Docker Essentials

 1. Docker Commands
 ```bash
docker ps                                   # See a list of all running containers
docker ps -a                                # See a list of all containers, even the ones not running
docker rm <hash>                            # Remove the specified container from this machine
docker rm $(docker ps -a -q)                # Remove all containers from this machine
docker images -a                            # Show all images on this machine
docker rmi <imagename>                      # Remove the specified image from this machine
docker rmi $(docker images -q)              # Remove all images from this machine
```

**If you have Docker desktop you can view the images and the containers in the app.**

2. Docker build
* Tells Docker: “Build an image from a Dockerfile.”
* Docker reads the Dockerfile in the current directory (or the directory you specify).
* `-t` is the tag that names your image. Here since I am pushing to dockerhub, dockerhub_username / image_name
* latest is like a label. you can use v1, v2, etc.
* the dot specifies the folder Docker will use for building the image. `. = current directory`. Docker looks for Dockerfile in this directory.
```bash
docker build -t batman771/loaneligibility:latest .
```

3. Docker Run

Starts a container from an image. `-p` maps a port from the container to your host machine. `8501` (host) → `8501` (container). This is needed because containers have their own network and cannot be accessed directly from your host machine unless ports are mapped. 
`-d` run the container in detached mode (or in the background) or your terminal is tied to it always. You can stop it from Docker_desktop > Containers > Stop

```bash
docker run -d -p 8501:8501 batman771/loaneligibility:latest
```

4. Docker Push

If the container runs smoothly locally, we can push it to DockerHub. [My repo link>](https://hub.docker.com/repositories/batman771?_gl=1*xtyxv*_gcl_au*NzA5NzQ5MjI4LjE3Njk1NDk1OTg.*_ga*Nzk0OTYzMzEwLjE3Njk1NDk1ODE.*_ga_XJWPQMJYHQ*czE3Njk1NTgxOTkkbzMkZzEkdDE3Njk1NTg1OTYkajUzJGwwJGgw)
```bash
docker push batman771/loaneligibility:latest
```

5. Docker Pull

Once an image is in the public repo, you can pull any image and run it. First delete the image (and any running container with that image) and pull the image again from the public repo. And run it.
```bash
docker pull batman771/loaneligibility:latest
```

## CI Essentials
This yaml code can be found on GitHub > Actions. Visit [GitHub > Actions](https://github.com/swapnilin/Credit_Eligibility_Application_with_Streamlit/actions/new), and look for 'Python Application' and click on Configure.

1. Understanding the ci.yaml code
This tells the GitHub actions to execute the flow only when there is push or pull request on the 'main' branch. You can also specify multiple branches as shown in the pull_request.
```bash
on:
  push:
    branches:
      -main
  pull_request:
    branches:
      -main
      -branch1
```

Linting scan your Python code for errors, bad practices, and syntax issues without running the code. flake8 checks your code without executing it, which means:
* Faster feedback
* Fewer runtime surprises

```bash
name: lint with flake8
```
Examples of issues CI should block:

| Category         | Example                           |
| ---------------- | --------------------------------- |
| Syntax issues    | Missing imports, unused variables |
| Logical smells   | Shadowed variables                |
| Bugs             | Referencing undefined names       |
| Style violations | Inconsistent formatting           |
| Dead code        | Imports never used                |

Example that tests might miss:

```bash
import numpy as np  # unused

def predict(x):
    return y + 1  # y is undefined
```
* flake8 fails immediately
* pytest might never reach this path

This pytest_test.py file has all the tests that need to be carried out after every updated to the code.
```bash
- name: run tests
      run: |
        pytest _test.py
```

#### Thank you for using the Credit Eligibility Application! Feel free to share your feedback.