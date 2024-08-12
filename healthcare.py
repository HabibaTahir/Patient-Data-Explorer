import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv("D:/ai and data science course/MACHINE LEARNING MIAN PROJECT/health _care/healthcare_dataset.csv")
    return data

# Load the data
data = load_data()

# Title of the app
st.title("Healthcare Data Finder")

# User inputs
st.sidebar.header("Input Patient Details")
name_input = st.sidebar.text_input("Name")
age_input = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
condition_input = st.sidebar.text_input("Medical Condition")
doctor_input = st.sidebar.text_input("Doctor's Name")
hospital_input = st.sidebar.text_input("Hospital's Name")

# Filter data based on user input
filtered_data = data

if name_input:
    filtered_data = filtered_data[filtered_data['Name'].str.contains(name_input, case=False)]
if age_input:
    filtered_data = filtered_data[filtered_data['Age'] == age_input]
if condition_input:
    filtered_data = filtered_data[filtered_data['Medical Condition'].str.contains(condition_input, case=False)]
if doctor_input:
    filtered_data = filtered_data[filtered_data['Doctor'].str.contains(doctor_input, case=False)]
if hospital_input:
    filtered_data = filtered_data[filtered_data['Hospital'].str.contains(hospital_input, case=False)]

# Display data
st.header("Filtered Healthcare Data")
st.write(f"Displaying {len(filtered_data)} rows of data")
st.dataframe(filtered_data)
