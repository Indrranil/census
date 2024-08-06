import os
import sys
import pandas as pd

# Adjust the path to the `data` directory
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, '..', 'data')

def load_data(file_name):
    """Load raw data from a CSV file."""
    file_path = os.path.join(data_dir, 'raw', file_name)
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean and preprocess the data."""
    # Example: Drop rows with missing values
    df.dropna(inplace=True)
    # Example: Convert column names to lowercase
    df.columns = [col.lower() for col in df.columns]
    return df

def save_data(df, file_name):
    """Save processed data to a CSV file."""
    file_path = os.path.join(data_dir, 'processed', file_name)
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    raw_data_file = 'population_data.csv'
    processed_data_file = 'population_data.csv'

    df = load_data(raw_data_file)
    df = clean_data(df)
    save_data(df, processed_data_file)
