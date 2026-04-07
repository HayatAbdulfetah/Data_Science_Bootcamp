import math
from collections import Counter

class StatEngine:
    def __init__(self, data):
        if not data:
            raise ValueError("Dataset cannot be empty.")

        # Clean data (only numeric)
        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise TypeError("No valid numeric data found.")

    def _clean_data(self, data):
        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(float(x))
            else:
                raise TypeError(f"Invalid data type detected: {x}")
        return cleaned

    # -------------------------
    # Central Tendency
    # -------------------------

    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self):
        counts = Counter(self.data)
        max_freq = max(counts.values())

        if max_freq == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in counts.items() if v == max_freq]
        return modes

    # -------------------------
    # Dispersion
    # -------------------------

    def get_variance(self, is_sample=True):
        n = len(self.data)
        mean = self.get_mean()

        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")

        denominator = (n - 1) if is_sample else n

        variance = sum((x - mean) ** 2 for x in self.data) / denominator
        return variance

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # -------------------------
    # Outlier Detection
    # -------------------------

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        outliers = [
            x for x in self.data
            if abs(x - mean) > threshold * std
        ]
        return outliers
