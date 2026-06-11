import streamlit as st

st.title("Resume Screening System")

resume = st.text_area("Paste Resume Text Here")

if st.button("Predict"):
    st.write("Prediction will appear here.")
