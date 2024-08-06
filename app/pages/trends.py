import os
import sys
import streamlit as st

# Set up paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, '..', '..', 'data', 'processed')

# Import functions from src
sys.path.insert(0, os.path.abspath(os.path.join(base_dir, '..', '..', 'src')))
from visualization import plot_trends

def trends():
    st.title("Trends")
    plot_trends(data_dir)
