import streamlit as st
import pandas as pd

def app():
    st.title("Add Instructor")
    st.markdown("### Add a New Instructor")

    with st.form("instructor_form"):
        fiscode = st.text_input('FisCode')
        first_name = st.text_input('First Name')
        last_name = st.text_input('Last Name')
        birthdate = st.date_input('Birth Date')
        email = st.text_input('Email')
        telephone = st.text_input('Telephone (Optional)', value='')

        submitted = st.form_submit_button("Submit")

        if submitted:
            if not (fiscode and first_name and last_name and birthdate and email):
                st.error("Please fill in all required fields.")
            else:
                # Assuming data insertion is successful
                st.success(f"Instructor {first_name} {last_name} added successfully.")
