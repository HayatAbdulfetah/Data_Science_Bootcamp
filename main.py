from src.monte_carlo import simulate_crashes

def run_simulation():
    for days in [30, 365, 10000]:
        prob, crashes = simulate_crashes(days)
        print(f"Days: {days}")
        print(f"Crashes: {crashes}")
        print(f"Simulated Probability: {prob:.4f}")
        print("-" * 30)

if __name__ == "__main__":
    run_simulation()
