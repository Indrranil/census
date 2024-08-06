import os

def get_data_path(file_name):
    """Construct path to the data file."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, '..', 'data', 'processed')
    return os.path.join(data_dir, file_name)
