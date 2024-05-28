import sys
import os
import unittest
from src.data_processor import DataProcessor
from src.anomaly_detector import AnomalyDetector
from src.report_generator import ReportGenerator
from src.model import Model

class TestModel(unittest.TestCase):
    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
    
    def tearDown(self):
        sys.path.pop(0)

    def test_run(self):
        processor = DataProcessor('data/data.csv')
        detector = AnomalyDetector()
        report_generator = ReportGenerator(None, None)
        model = Model(processor, detector, report_generator)
        model.run()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()