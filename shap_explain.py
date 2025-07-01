# shap_explain.py
import pandas as pd
import shap
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

# Step 1: Load dataset
df = pd.read_csv("training_data.csv")

# Drop non-numeric or irrelevant columns
X = df.drop(["label", "timestamp"], axis=1, errors='ignore')
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=42)

# Step 2: Train XGBoost
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Step 3: SHAP initialization
explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# Step 4: SHAP summary plot
shap.summary_plot(shap_values, X_test)
