# evaluate_node_model.py

import pandas as pd
import argparse
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# Parse arguments
parser = argparse.ArgumentParser(description="Evaluate a trained node model")
parser.add_argument('--model', required=True, help="Path to the trained model (.pkl)")
parser.add_argument('--data', required=True, help="Path to the corresponding node CSV data")
args = parser.parse_args()

# Load model and dataset
model = joblib.load(args.model)
df = pd.read_csv(args.data)

# Prepare features and labels
X = df.drop(["label", "timestamp"], axis=1, errors="ignore")
y = df["label"]

# Split into train/test for evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Predict and evaluate
y_pred = model.predict(X_test)

print(f"=== Evaluation for {args.model} ===")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
