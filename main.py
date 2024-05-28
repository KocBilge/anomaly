from src.data_processor import DataProcessor
from src.anomaly_detector import AnomalyDetector
from src.report_generator import ReportGenerator
from src.model import Model

def main():
    data_processor = DataProcessor("data/data.csv")
    anomaly_detector = AnomalyDetector()
    report_generator = ReportGenerator(None, None)

    model = Model(data_processor, anomaly_detector, report_generator)
    model.run()

if __name__ == "__main__":
    main()
