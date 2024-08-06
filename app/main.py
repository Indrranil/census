import streamlit as st
import pandas as pd
from src.visualization import plot_age_distribution, plot_gender_ratio

def load_data():
    """Load the processed data."""
    return pd.read_csv('data/processed/population_data.csv')

def main():
    st.title("Census Data Insight Dashboard")

    # Sidebar for navigation
    st.sidebar.header("Navigation")
    page = st.sidebar.radio("Select a Page", ["Home", "Demographics", "Trends"])

    # Load data
    df = load_data()

    if page == "Home":
        st.write("Welcome to the Census Data Insight Dashboard!")

    elif page == "Demographics":
        st.subheader("Demographic Analysis")
        st.write("### Age Distribution")
        age_fig = plot_age_distribution(df)
        st.plotly_chart(age_fig)

        st.write("### Gender Ratio")
        gender_fig = plot_gender_ratio(df)
        st.plotly_chart(gender_fig)

    elif page == "Trends":
        st.subheader("Trend Analysis")
        st.write("This page will contain trend analysis visualizations.")

if __name__ == "__main__":
    main()
