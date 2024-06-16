import streamlit as st
import pandas as pd

def app():
    st.title("Add Lesson")
    st.markdown("### Add a New Lesson")

    # Example data for dropdowns
    instructors_data = {'FisCode': ['F001', 'F002', 'F003']}
    df_instructors = pd.DataFrame(instructors_data)

    courses_data = {'Course Code': ['C101', 'C102', 'C103']}
    df_courses = pd.DataFrame(courses_data)

    with st.form("lesson_form"):
        fiscode = st.selectbox('Instructor FisCode', df_instructors['FisCode'])
        day = st.selectbox('Day', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        start_time = st.slider('Start Time (hour)', 0, 23, 9)
        duration = st.slider('Duration (minutes)', 1, 60, 30)
        course_code = st.selectbox('Course Code', df_courses['Course Code'])
        room = st.text_input('Room')

        submitted = st.form_submit_button("Submit")

        if submitted:
            if duration > 60:
                st.error("Duration cannot be more than 60 minutes.")
            else:
                # Assuming data insertion is successful
                st.success(f"Lesson for course {course_code} added successfully.")
