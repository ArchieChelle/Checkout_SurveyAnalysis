# scripts/run_analysis.py
import pandas as pd
from src.analysis import compute_mean_std
import config

df = pd.read_csv(config.PROCESSED_DATA_PATH)
mean, std = compute_mean_std(df, config.EASE_COL)
print(f"Mean Ease of Checkout: {mean:.2f}, Std: {std:.2f}")
