import streamlit as st
import pandas as pd
import joblib

model = joblib.load("student_marks_model.pkl")

st.title("🎓 Student Final Marks Predictor")
st.write("Enter student details to predict final marks.")

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value = None,
    placeholder = "0"
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value = None,
    placeholder = "0"
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value = None,
    placeholder = "0"
)

assignment_score = st.number_input(
    "Assignment Score",
    min_value=0.0,
    max_value=100.0,
    value = None,
    placeholder = "0"   
)


if st.button("Predict Final Marks"):

    if (
        study_hours is None
        or attendance is None
        or previous_marks is None
        or assignment_score is None
    ):
        st.warning("Please enter all the details.")

    else:
        user_data = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance": attendance,
            "previous_marks": previous_marks,
            "assignment_score": assignment_score
        }])

        prediction = model.predict(user_data)[0]

        # Keep marks between 0 and 100
        prediction = max(0, min(100, prediction))



        st.subheader("🎯 Prediction Result")

        st.metric(
            label="Predicted Final Marks",
            value=f"{prediction:.2f} / 100"
        )

        if prediction >= 80:
            st.success("🎉 Excellent performance!")

        elif prediction >= 60:
            st.info("👍 Good performance!")

        elif prediction >= 40:
            st.warning("📚 Average performance. Keep improving!")

        else:
            st.error("💪 Needs improvement. Keep working hard!")