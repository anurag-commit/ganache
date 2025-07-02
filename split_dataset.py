# split_dataset.py

import pandas as pd
import numpy as np

# Load your full dataset
df = pd.read_csv("training_data.csv")

# Shuffle to randomize rows
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split into 3 equal parts for 3 nodes
node1, node2, node3 = np.array_split(df, 3)

# Save each part as a new CSV
node1.to_csv("node1_data.csv", index=False)
node2.to_csv("node2_data.csv", index=False)
node3.to_csv("node3_data.csv", index=False)

print("✅ Dataset split into 3 parts: node1_data.csv, node2_data.csv, node3_data.csv")
