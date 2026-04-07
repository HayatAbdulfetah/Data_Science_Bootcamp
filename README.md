# Statistical Engineering & Simulation Project

## Project Overview

This project implements a pure Python statistical engine (`StatEngine`) built from scratch using only standard libraries. The engine processes raw 1D numerical data and computes key statistical measures such as mean, median, mode, variance, standard deviation, and outliers.

In addition, the project includes a Monte Carlo simulation to model a real-world probabilistic scenario (server crashes) and demonstrate the Law of Large Numbers (LLN).

The goal is to combine strong coding practices, mathematical correctness, and statistical reasoning.

---

## Mathematical Logic

### Mean
The mean is calculated as:

Mean = (Sum of all values) / (Number of values)

---

### Median

- If the dataset length is **odd**, the median is the middle value after sorting.
- If the dataset length is **even**, the median is the average of the two middle values.

---

### Mode

- The mode is the value(s) that appear most frequently.
- If multiple values share the highest frequency, all are returned (multimodal case).
- If all values are unique, the engine returns:
  
  "No mode (all values are unique)"

---

### Variance

Variance measures how far data points spread from the mean.

- **Population Variance**:
  
  Variance = Σ(x - mean)² / n

- **Sample Variance (Bessel’s Correction)**:
  
  Variance = Σ(x - mean)² / (n - 1)

Bessel’s correction (n-1) is used to reduce bias when working with sample data.

---

### Standard Deviation

Standard deviation is the square root of variance:

Standard Deviation = √Variance

It represents how spread out the data is.

---

### Outlier Detection

Outliers are defined as values that are far from the mean:

A data point is considered an outlier if:

|x - mean| > threshold × standard deviation

(Default threshold = 2)

---

## Project Structure

statistical_engine/
│
├── data/
│ └── sample_salaries.json
├── src/
│ ├── init.py
│ ├── stat_engine.py
│ └── monte_carlo.py
├── tests/
│ ├── init.py
│ └── test_stat_engine.py
├── README.md
└── main.py


---

## Setup Instructions

1. Clone the repository:

```bash
git clone <your-repository-link>
Navigate into the project:

cd statistical_engine
Run the main program:

python main.py
Running Tests
To run the unit tests using Python’s built-in unittest:

python -m unittest discover tests
Monte Carlo Simulation & Law of Large Numbers
The simulation models a server with a 4.5% daily crash probability.

The function simulate_crashes(days) runs experiments over different time periods:

30 days

365 days

10,000 days

Interpretation:
According to the Law of Large Numbers (LLN):

Small sample sizes (e.g., 30 days) produce highly variable results.

Larger sample sizes (e.g., 10,000 days) converge toward the true probability (0.045).

This demonstrates that:

Experimental probability becomes more reliable as the number of trials increases.

Why Small Data is Dangerous
Using only a small dataset (like 30 days) to estimate yearly server failures is risky because:

Results are highly affected by randomness

Not representative of long-term behavior

Can lead to incorrect budgeting decisions

Example:

30 days → very few crashes → underestimation

Real yearly expectation → significantly higher crashes

Acceptance Criteria Checklist

 Handles empty datasets (prevents crashes)

 Handles invalid/mixed data types with clear errors

 Correct mean calculation

 Correct median (even and odd cases)

 Mode supports multimodal distributions

 Returns message when no mode exists

 Implements both sample and population variance

 Correct standard deviation calculation

 Outlier detection using standard deviation

 Monte Carlo simulation implemented

 Unit tests included and passing

 Testing Coverage

The unit tests verify:

Mean correctness
Median correctness (odd vs even datasets)
Proper error handling for empty input
Standard deviation against known values