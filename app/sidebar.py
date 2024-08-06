import streamlit as st

def show_sidebar():
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Select a Page", ["Home", "Demographics", "Trends"])
    return page
