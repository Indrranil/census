import os
import sys
import pandas as pd
import plotly.express as px

# Import utils for path handling
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from utils import get_data_path

def plot_demographics(data_dir):
    """Plot demographic data."""
    file_path = get_data_path('population_data.csv')
    df = pd.read_csv(file_path)

    fig_age = px.histogram(df, x="age", title="Age Distribution")
    fig_gender = px.pie(df, names="gender", title="Gender Ratio")

    fig_age.show()
    fig_gender.show()

def plot_trends(data_dir):
    """Plot trends data (example placeholder)."""
    file_path = get_data_path('population_data.csv')
    df = pd.read_csv(file_path)

    # Example plot
    fig = px.line(df, x="date", y="value", title="Trends Over Time")
    fig.show()
