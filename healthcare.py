import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def get_mock_data():
    data = {
        'age': [25, 30, 45, 10, 60, 5, 22, 80, 15, 35],
        'days_of_fever': [3, 5, 2, 7, 4, 6, 3, 2, 8, 4],
        'platelet_count': [150000, 80000, 120000, 40000, 90000, 30000, 140000, 110000, 20000, 95000],
        'hematocrit_pct': [40, 48, 42, 52, 45, 55, 38, 41, 58, 44],
        'warning_signs': [0, 1, 0, 1, 1, 1, 0, 0, 1, 1],
        'outcome': [0, 1, 0, 1, 1, 1, 0, 0, 1, 1] 
    }
    return pd.DataFrame(data)

class DengueDecisionSystem:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.is_trained = False

    def train(self, df):
        X = df.drop('outcome', axis=1)
        y = df['outcome']
        self.model.fit(X, y)
        self.is_trained = True

    def classify_patient(self, patient_df):
        if not self.is_trained: return "Error", 0.0
        prob = self.model.predict_proba(patient_df)[0][1]
        plt = patient_df['platelet_count'].values[0]
        hct = patient_df['hematocrit_pct'].values[0]
        
        if prob > 0.5 or plt < 50000 or hct > 50:
            return "CRITICAL: Immediate Hospitalization Required", prob
        elif plt < 100000:
            return "HIGH RISK: Close Monitoring Needed", prob
        elif plt > 270000:
            return "HIGH RISK: Close Monitoring Needed", prob
        else:
            return "STABLE: Home Management with Follow-up", prob

    def get_risk_trend(self, base_patient_df):
        plt_range = np.linspace(10000, 200000, 50)
        trend_data = []
        for p in plt_range:
            temp_df = base_patient_df.copy()
            temp_df['platelet_count'] = p
            prob = self.model.predict_proba(temp_df)[0][1]
            trend_data.append({"Platelet Count": p, "Risk Probability": prob})
        return pd.DataFrame(trend_data)
    