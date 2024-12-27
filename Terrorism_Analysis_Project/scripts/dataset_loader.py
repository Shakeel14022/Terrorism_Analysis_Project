import pandas as pd

def load_dataset():
    """
    Loads the dataset from the dataset folder and returns it as a pandas DataFrame.
    """
    file_path = 'Terrorism_Analysis_Project/dataset/globalterrorismdatabase_1970_2020_F.csv'
    try:
        data = pd.read_csv(file_path, low_memory=False)
        print("Dataset loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"File not found. Please check the file path: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")
        return None


