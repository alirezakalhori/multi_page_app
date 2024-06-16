import streamlit as st
import pandas as pd
import datetime

def app():
    st.title("Instructors")
    st.markdown("### View Available Instructors")

    # Example data
    instructors_data = {
        'FisCode': ['F001', 'F002', 'F003'],
        'First Name': ['Alice', 'Bob', 'Charlie'],
        'Last Name': ['Smith', 'Johnson', 'Williams'],
        'BirthDate': ['1980-05-01', '1975-07-23', '1988-11-12'],
        'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com']
    }
    df_instructors = pd.DataFrame(instructors_data)

    # Filter by last name
    last_name_filter = st.text_input('Filter by Last Name')
    if last_name_filter:
        df_instructors = df_instructors[df_instructors['Last Name'].str.contains(last_name_filter, case=False)]

    # Filter by birth date range
    start_date = st.date_input('Start Date', value=datetime.date(1970, 1, 1))
    end_date = st.date_input('End Date', value=datetime.date.today())
    df_instructors['BirthDate'] = pd.to_datetime(df_instructors['BirthDate'])
    df_instructors = df_instructors[(df_instructors['BirthDate'] >= start_date) & (df_instructors['BirthDate'] <= end_date)]

    if not df_instructors.empty:
        for _, row in df_instructors.iterrows():
            st.write(f"**{row['First Name']} {row['Last Name']}**")
            st.write(f"Birth Date: {row['BirthDate'].date()}")
            st.write(f"Email: {row['Email']}")
            st.write("---")
    else:
        st.warning("No instructors found with the selected criteria.")
