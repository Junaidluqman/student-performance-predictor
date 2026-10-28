# Student Performance Predictor

## About the Project
Student Performance Predictor is a beginner-friendly Machine Learning project developed using Python. It predicts whether a student may be at risk of failing based on academic and personal study-related information.

The project includes a web interface built with Streamlit, allowing users to enter student details and receive a prediction from a trained Machine Learning model.

## Objectives
- Practice data analysis using Pandas and NumPy.
- Understand Machine Learning classification.
- Build a web application using Streamlit.
- Learn how to integrate a trained ML model into a web app.
- Develop and publish a complete Data Science project.

## Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## Machine Learning
The project uses Logistic Regression to classify students into two categories:

- **Not at risk of failing:** Predicted class 0.
- **At risk of failing:** Predicted class 1.

The model was trained using the UCI Student Performance dataset. Previous-period grades were excluded from the input features to reduce target leakage.

## Project Structure

```text
student-performance-webapp/
├── app.py
├── student_performance_model.pkl
├── feature_metadata.json
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-performance-webapp
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Dataset
UCI Machine Learning Repository — Student Performance:

https://archive.ics.uci.edu/dataset/320/student+performance

## Limitations
Predictions are estimates and may be incorrect. The model is intended for educational purposes and should not be used to make important decisions about students.

## Author
BS Information Technology Student | Data Science & Machine Learning Learner

## Disclaimer
This is an educational project developed to practice data analysis, Machine Learning, and web application development.
