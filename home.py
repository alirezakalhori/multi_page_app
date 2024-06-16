import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("Home Page")
    st.markdown("""
    ## Welcome to the Course Management System
    This application allows you to manage and view course schedules and instructors.
    """)

    # Example data
    data = {
        'Time Slot': ['Morning', 'Afternoon', 'Evening'],
        'Number of Lessons': [10, 15, 5]
    }
    df_time_slot = pd.DataFrame(data)

    data_day = {
        'Day of Week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'Number of Lessons': [8, 12, 15, 9, 11]
    }
    df_day = pd.DataFrame(data_day)

    # Bar chart
    st.subheader("Number of Lessons for Each Time Slot")
    fig, ax = plt.subplots()
    ax.bar(df_time_slot['Time Slot'], df_time_slot['Number of Lessons'])
    st.pyplot(fig)

    # Area chart
    st.subheader("Number of Scheduled Lessons Based on Day of the Week")
    fig, ax = plt.subplots()
    ax.fill_between(df_day['Day of Week'], df_day['Number of Lessons'], color="skyblue", alpha=0.4)
    ax.plot(df_day['Day of Week'], df_day['Number of Lessons'], color="Slateblue", alpha=0.6)
    st.pyplot(fig)
