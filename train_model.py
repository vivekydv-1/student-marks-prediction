import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("student_marks_150.csv")


# ==========================================
# 2. Select Features and Target
# ==========================================

X = df[[
    "study_hours",
    "attendance",
    "previous_marks",
    "assignment_score"
]]

y = df["final_marks"]


# ==========================================
# 3. Split Data into Training and Testing
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 4. Train Linear Regression Model
# ==========================================

model = LinearRegression()

model.fit(X_train, y_train)

print("Model trained successfully!")


# ==========================================
# 5. Test Model with Example Student
# ==========================================

student_marks = {
    "study_hours": 6,
    "attendance": 90,
    "previous_marks": 85,
    "assignment_score": 80
}

example_student = pd.DataFrame([student_marks])

example_prediction = model.predict(example_student)

print(
    "Example Predicted Final Marks:",
    example_prediction[0]
)


# ==========================================
# 6. Make Predictions on Test Data
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 7. Evaluate Model
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print("MAE:", mae)
print("R² Score:", r2)


# ==========================================
# 8. Actual vs Predicted Marks
# ==========================================

print("\nActual Marks:")
print(list(y_test))

print("\nPredicted Marks:")
print(list(y_pred))


# ==========================================
# 9. Scatter Plot
# ==========================================

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted Marks")

plt.show()

joblib.dump(model, "student_marks_model.pkl")

print("Model saved successfully!")