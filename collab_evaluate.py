import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Load models
model1 = joblib.load("node1_model.pkl")
model2 = joblib.load("node2_model.pkl")
model3 = joblib.load("node3_model.pkl")

# Load full dataset
df = pd.read_csv("training_data.csv")
X = df.drop(["label", "timestamp"], axis=1, errors="ignore")
y = df["label"]

# Split into test set
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Get probability predictions from each model
probs1 = model1.predict_proba(X_test)
probs2 = model2.predict_proba(X_test)
probs3 = model3.predict_proba(X_test)

# Soft voting
avg_probs = (probs1 + probs2 + probs3) / 3.0
final_preds = np.argmax(avg_probs, axis=1)

# Evaluate
conf_matrix = confusion_matrix(y_test, final_preds)
report = classification_report(y_test, final_preds)
acc = accuracy_score(y_test, final_preds)

# Print to console
print("=== Collaborative Voting Evaluation ===")
print("Confusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(report)
print(f"Accuracy: {acc:.4f}")

# Save to file
with open("collab_results.txt", "w") as f:
    f.write("=== Collaborative Voting Evaluation ===\n")
    f.write("Confusion Matrix:\n")
    f.write(str(conf_matrix) + "\n\n")
    f.write("Classification Report:\n")
    f.write(report + "\n")
    f.write(f"Accuracy: {acc:.4f}\n")

print("\n✅ Results saved to collab_results.txt")
