import streamlit as st
import pandas as pd

st.title("Charts")

st.write("This page shows a simple chart.")

data = pd.DataFrame({
    "City": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "Visitors": [120, 95, 80, 70]
})

st.bar_chart(
    data.set_index("City")
)

show_table = st.checkbox("Show data table")

if show_table:
    st.dataframe(data)
