import streamlit as st
import pyperclip

st.title("Rocket Calculator")
st.subheader("Millimeters to Inches")

mm = st.text_input(label="Enter millimeters", value="")
if st.button("Convert") and mm is not None:
    inches = round(float(mm)/25.4,4)

    st.code(inches, language="python")

