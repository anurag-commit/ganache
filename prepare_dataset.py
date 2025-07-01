import pandas as pd

# Load the JSON file with all blocks
df = pd.read_json("all_blocks.json")

# Convert timestamp to datetime for readability (optional)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# Compute interval between consecutive blocks
df["interval"] = df["timestamp"].diff().dt.total_seconds().fillna(0)

# Label attack blocks (you can change 116 as per your real attack block number)
df["label"] = df["number"].apply(lambda x: 1 if x >= 116 else 0)

# Save to CSV
df.to_csv("training_data.csv", index=False)
