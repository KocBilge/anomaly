from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(contamination=contamination)
        
    def train_model(self, data):
        self.model.fit(data)
        
    def detect_anomalies(self, data):
        predictions = self.model.predict(data)
        return predictions        