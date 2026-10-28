import json
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓"
)

# Load model and input information
model = joblib.load("student_performance_model.pkl")

with open("feature_metadata.json", "r") as file:
    metadata = json.load(file)

st.title("🎓 Student Performance Predictor")
st.write("Enter student details to predict academic risk.")

inputs = {}

with st.form("student_form"):
    for col, info in metadata.items():
        if info["type"] == "number":
            minimum = info["min"]
            maximum = info["max"]

            if minimum == maximum:
                inputs[col] = minimum
            else:
                inputs[col] = st.number_input(
                    col.replace("_", " ").title(),
                    min_value=minimum,
                    max_value=maximum,
                    value=info["default"]
                )
        else:
            options = info["options"]
            default = info["default"]

            inputs[col] = st.selectbox(
                col.replace("_", " ").title(),
                options,
                index=options.index(default)
            )

    submitted = st.form_submit_button("Predict")

if submitted:
    input_df = pd.DataFrame([inputs])
    prediction = int(model.predict(input_df)[0])

    if prediction == 1:
        st.warning("Prediction: At risk of failing")
    else:
        st.success("Prediction: Not at risk of failing")

    st.caption(
        "This is a machine learning estimate, "
        "not a guarantee of academic performance."
    )