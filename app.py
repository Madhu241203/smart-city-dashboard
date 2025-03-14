import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("smart_city_real_time_analytics_enhanced.csv")  
    return df
df = load_data()
st.title(" Smart City Crime Monitoring Dashboard")
crime_types = df["crime_type"].unique()
selected_crime = st.sidebar.selectbox("Select Crime Type", crime_types)
filtered_df = df[df["crime_type"] == selected_crime]
st.subheader(f"Crime Data for {selected_crime}")
st.dataframe(filtered_df)
st.subheader(" Crime Trend Over Time")
fig, ax = plt.subplots()
filtered_df["timestamp"] = pd.to_datetime(filtered_df["timestamp"])
filtered_df.groupby(filtered_df["timestamp"].dt.date).size().plot(kind="line", ax=ax)
st.pyplot(fig)
high_severity = filtered_df[filtered_df["severity"] >= 4]
if not high_severity.empty:
    st.warning(" High severity crimes detected!") where should i have to type this code