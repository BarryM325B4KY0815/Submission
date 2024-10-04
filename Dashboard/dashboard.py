import streamlit as st
import pandas as pd

# Title and description
st.title("Basic Bike Sharing Dashboard")
st.write("This dashboard provides a summary of bike sharing data.")

# File uploader for CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Load data if a file is uploaded
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding='utf-8')
    
    # Display data overview
    st.subheader("Data Overview")
    st.write(data.head())

    # Show basic statistics
    st.subheader("Summary Statistics")
    st.write(data.describe())

    # Create a line chart for total count of bike rentals
    st.subheader("Total Bike Rentals Over Time")
    st.line_chart(data[['dteday', 'cnt']].set_index('dteday'))

    # Create a bar chart for average rentals per season
    season_avg = data.groupby('season')['cnt'].mean().reset_index()
    st.subheader("Average Bike Rentals per Season")
    st.bar_chart(season_avg.set_index('season'))

    # Filter by working day
    st.subheader("Filter by Working Day")
    working_day_filter = st.selectbox("Choose Working Day", options=data['workingday'].unique())
    filtered_data = data[data['workingday'] == working_day_filter]
    st.write(filtered_data)

    # Display weather conditions
    st.subheader("Weather and Bike Rentals")
    st.scatter_chart(data[['temp', 'cnt']])
else:
    st.write("Please upload a CSV file to proceed.")
