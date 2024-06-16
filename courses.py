import streamlit as st
import pandas as pd

def app():
    st.title("Courses")
    st.markdown("### View and Filter Available Courses")

    # Example data
    courses_data = {
        'Course Code': ['C101', 'C102', 'C103'],
        'Course Name': ['Mathematics', 'Physics', 'Chemistry'],
        'Course Type': ['Core', 'Elective', 'Core'],
        'Level': [1, 2, 1]
    }
    df_courses = pd.DataFrame(courses_data)

    # Metrics
    num_courses = df_courses.shape[0]
    num_types = df_courses['Course Type'].nunique()
    st.metric(label="Number of Courses", value=num_courses)
    st.metric(label="Distinct Course Types", value=num_types)

    # Filtering options
    selected_types = st.multiselect('Course Type', df_courses['Course Type'].unique())
    level_range = st.slider('Level Range', 1, 4, (1, 2))

    # Filter dataframe
    if selected_types:
        df_courses = df_courses[df_courses['Course Type'].isin(selected_types)]
    df_courses = df_courses[df_courses['Level'].between(*level_range)]

    if not df_courses.empty:
        st.dataframe(df_courses)
    else:
        st.warning("No courses found with the selected criteria.")
