import streamlit as st
import joblib

model = joblib.load("resume_classifier.pkl")

st.title("Resume Screening System")

resume_text = st.text_area(
    "Paste Resume Text",
    height=300
)

if st.button("Predict Category"):

    if resume_text:

        prediction = model.predict(
            [resume_text]
        )[0]

        st.success(
            f"Predicted Category: {prediction}"
        )
