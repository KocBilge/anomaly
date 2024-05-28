import unittest
from src.anomaly_detector import AnomalyDetector
from src.data_processor import DataProcessor

class TestAnomalyDetector(unittest.TestCase):
    def test_anomaly_detection(self):
        processor = DataProcessor('data/data.csv')
        processor.load_data()
        processed_data = processor.preprocess_data()

        detector = AnomalyDetector()
        detector.train_model(processed_data)
        predictions = detector.detect_anomalies(processed_data)
        
        self.assertEqual(len(predictions), len(processed_data))

if __name__ == '__main__':
    unittest.main()