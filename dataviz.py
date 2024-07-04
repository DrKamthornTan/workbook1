import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the data
df = pd.read_csv('workbook1.csv')

# Streamlit app
st.title("DHV Histogram Plot")

# Add sidebar
st.sidebar.title("Choose Axes")
x_axis = st.sidebar.selectbox("X-axis", options=df.columns)
y_axis = st.sidebar.selectbox("Y-axis", options=df.columns)

# Display the dataframe
st.subheader("Data")
st.write(df)

# Create the histogram
st.subheader("Histogram")
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(data=df, x=x_axis, ax=ax)
st.pyplot(fig)

# Create the count plot
#st.subheader("Count Plot")
#fig, ax = plt.subplots(figsize=(12, 6))
#sns.countplot(data=df, x=x_axis, ax=ax)
#st.pyplot(fig)