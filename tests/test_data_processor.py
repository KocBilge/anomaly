import unittest
from src.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def test_load_data(self):
        processor = DataProcessor('data/data.csv')
        data = processor.load_data()
        self.assertIsNotNone(data)

    def test_preprocess_data(self):
        processor = DataProcessor('data/data.csv')
        processor.load_data()
        processed_data = processor.preprocess_data()
        self.assertIsNotNone(processed_data)

if __name__ == '__main__':
    unittest.main()