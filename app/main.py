import os
import sys
import streamlit as st
from sidebar import sidebar.show_sidebar

# Set up paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, '..', 'data', 'processed')

# Import functions from src
sys.path.insert(0, os.path.abspath(os.path.join(base_dir, '..', 'src')))
from visualization import plot_demographics, plot_trends

# Sidebar
sidebar()

# Streamlit app structure
def main():
    st.title("Census Data Insight Dashboard")

    # Navigation
    page = st.sidebar.selectbox("Choose a page", ["Home", "Demographics", "Trends"])

    if page == "Home":
        st.write("Welcome to the Census Data Insight Dashboard!")
    elif page == "Demographics":
        plot_demographics(data_dir)
    elif page == "Trends":
        plot_trends(data_dir)

if __name__ == "__main__":
    main()
