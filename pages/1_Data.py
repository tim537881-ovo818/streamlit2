import streamlit as st
import pandas as pd

st.title("Data")

st.write("This page shows a simple example dataset.")

data = pd.DataFrame({
    "City": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "Temperature": [24, 22, 27, 26],
    "Visitors": [120, 95, 80, 70]
})

st.dataframe(data)

city = st.selectbox(
    "Choose a city",
    data["City"]
)

st.write("You selected:", city)
