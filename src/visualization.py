import plotly.express as px
import pandas as pd

def plot_age_distribution(df):
    """Create a bar chart of age distribution."""
    fig = px.histogram(df, x='age', title='Age Distribution')
    return fig

def plot_gender_ratio(df):
    """Create a pie chart of gender ratio."""
    gender_counts = df['gender'].value_counts()
    fig = px.pie(values=gender_counts, names=gender_counts.index, title='Gender Ratio')
    return fig

if __name__ == "__main__":
    # Example usage
    df = pd.read_csv('data/processed/population_data.csv')

    age_fig = plot_age_distribution(df)
    age_fig.show()

    gender_fig = plot_gender_ratio(df)
    gender_fig.show()
