from src.data_processor import DataProcessor
from src.anomaly_detector import AnomalyDetector
from src.report_generator import ReportGenerator

class Model:
    def __init__(self, data_processor, anomaly_detector, report_generator):
        self.data_processor = data_processor
        self.anomaly_detector = anomaly_detector
        self.report_generator = report_generator

    def run(self):
        data = self.data_processor.load_data()
        processed_data = self.data_processor.preprocess_data()
        self.anomaly_detector.train_model(processed_data)
        predictions = self.anomaly_detector.detect_anomalies(processed_data)
        self.report_generator.data = processed_data
        self.report_generator.predictions = predictions
        self.report_generator.generate_report()