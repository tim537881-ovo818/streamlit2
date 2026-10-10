import streamlit as st

st.set_page_config(
    page_title="Streamlit Multipage App",
    page_icon="👋",
)

st.title("Streamlit Multipage App")

st.write(
    """
    Welcome to my multipage Streamlit app.

    Use the sidebar to switch between the different pages.
    """
)

st.info("Select a page from the sidebar to get started.")
