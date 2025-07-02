
import pandas as pd
import argparse
import joblib
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np

# Load all models
model1 = joblib.load("node1_model.pkl")
model2 = joblib.load("node2_model.pkl")
model3 = joblib.load("node3_model.pkl")

# Load full dataset for shared evaluation
df = pd.read_csv("training_data.csv")

# Drop unused columns and split
X = df.drop(["label", "timestamp"], axis=1, errors="ignore")
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Get probability predictions from each node
probs1 = model1.predict_proba(X_test)
probs2 = model2.predict_proba(X_test)
probs3 = model3.predict_proba(X_test)

# Average probabilities (soft voting)
avg_probs = (probs1 + probs2 + probs3) / 3.0
final_preds = np.argmax(avg_probs, axis=1)

# Evaluation
print("=== Collaborative Voting Results ===")
print("Confusion Matrix:")
print(confusion_matrix(y_test, final_preds))
print("\nClassification Report:")
print(classification_report(y_test, final_preds))
