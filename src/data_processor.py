import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.processed_data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
        except pd.errors.EmptyDataError:
            print("CSV file is empty or contains no data.")

    def preprocess_data(self):
        scaler = StandardScaler()
        self.processed_data = scaler.fit_transform(self.data)
        return self.processed_data
