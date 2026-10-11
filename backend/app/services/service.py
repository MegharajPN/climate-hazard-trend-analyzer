from typing import List, Dict
import pandas as pd

class ClimateHazardTrendAnalyzer:
    def __init__(self, data_source: str):
        self.data_source = data_source
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        # Load data from the specified source
        return pd.read_csv(self.data_source)

    def detect_heatwaves(self, temperature_data: pd.Series, threshold: float) -> List[int]:
        # Detect heatwaves based on a temperature threshold
        heatwave_indices = []
        for i in range(len(temperature_data)):
            if temperature_data[i] > threshold:
                heatwave_indices.append(i)
        return heatwave_indices

    def analyze_trends(self, data: pd.DataFrame, column: str) -> Dict[str, float]:
        # Analyze trends in the specified column of the data
        trend_data = data[column].rolling(window=12).mean()  # Example: 12-month rolling average
        trend = trend_data.iloc[-1] - trend_data.iloc[0]
        return {
            "initial_value": trend_data.iloc[0],
            "final_value": trend_data.iloc[-1],
            "trend": trend
        }

    def get_heatwave_statistics(self, heatwave_indices: List[int]) -> Dict[str, int]:
        # Calculate statistics from detected heatwaves
        return {
            "total_heatwaves": len(heatwave_indices),
            "heatwave_days": len(set(heatwave_indices))
        }