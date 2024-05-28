import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, data, predictions):
        self.data = data
        self.predictions = predictions
        
    def generate_report(self):
        anomaly_data = self.data[self.predictions == -1]
        normal_data  = self.data[self.predictions == -1]
        
        plt.scatter(normal_data[:, 0], normal_data[:, 1], c='blue', label='Normal')
        plt.scatter(anomaly_data[:, 0], anomaly_data[:, 1], c='red', label='Anomaly')
        plt.legend()
        plt.show()