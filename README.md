# Student Marks Prediction 🎓

This is my beginner Machine Learning project where I built a model to predict a student's final marks.

I made this project while learning Python, Machine Learning and Streamlit.

## About the Project

The model predicts final marks using four things:

- Study Hours
- Attendance
- Previous Marks
- Assignment Score

I used a dataset containing 150 student records.

## Machine Learning

I tried three different models:

| Model | MAE | R² Score |
|---|---:|---:|
| Linear Regression | 2.51 | 0.890 |
| Random Forest | 3.11 | 0.837 |
| Decision Tree | 3.74 | 0.767 |

After comparing the models, **Linear Regression performed the best** on my test data.

### Final Model Results

- MAE: **2.51**
- R² Score: **0.890**

## Technologies I Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

## How the Project Works

Student Data  
↓  
Data Preprocessing  
↓  
Train/Test Split  
↓  
Linear Regression Model  
↓  
Model Evaluation  
↓  
Save Model  
↓  
Streamlit App  
↓  
Final Marks Prediction

## Streamlit App

The project has a simple Streamlit interface where a user can enter:

- Study Hours
- Attendance
- Previous Marks
- Assignment Score

After clicking **Predict Final Marks**, the application shows the predicted marks.

## How to Run

## First install the required libraries:

```pip install -r requirements.txt` ```

## Train the Model:

```python train_model.py` ```

## After that, run the Streamlit app:

```python -m streamlit run app.py` ``` 

Then, The app will Run in browser.

## Project Files

student-marks-prediction/
 app.py
── train_model.py
── requirements.txt
── student_marks_150.csv
── README.md

## What I Learned
While making this project, I learned about:

Loading datasets using Pandas
Splitting data into training and testing sets
Training a Linear Regression model
Making predictions
Evaluating a model using MAE and R²
Creating an Actual vs Predicted graph
Saving a trained model using Joblib
Creating a simple ML web app using Streamlit
Future Improvements

In the future, I would like to:

Use a larger dataset
Try more Machine Learning models
Improve the model accuracy
Add more features
Deploy the Streamlit app online
Author

Vivek Yadav

B.Tech IT Student | Learning Python & Machine Learning








