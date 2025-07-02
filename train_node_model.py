
import pandas as pd
import argparse
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Train model on node data")
parser.add_argument('--data', required=True, help="Path to node data CSV")
parser.add_argument('--out', required=True, help="Path to save trained model (.pkl)")
args = parser.parse_args()

# Load dataset
df = pd.read_csv(args.data)

# Drop unused columns (like timestamp if present)
X = df.drop(["label", "timestamp"], axis=1, errors="ignore")
y = df["label"]

# Split data for training and internal validation
X_train, X_val, y_train, y_val = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, args.out)

print(f"✅ Model trained and saved to {args.out}")
