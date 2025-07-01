# train_ensemble.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings("ignore")

# Step 1: Load the dataset
df = pd.read_csv("training_data.csv")

# Step 2: Drop non-numeric or irrelevant columns
columns_to_drop = ["label", "timestamp"]
X = df.drop(columns=columns_to_drop, errors='ignore')  # errors='ignore' handles missing cols gracefully
y = df["label"]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.3, random_state=42
)

# Step 4: Define models
rf = RandomForestClassifier(random_state=42)
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
ada = AdaBoostClassifier(random_state=42)
lr = LogisticRegression(max_iter=1000, random_state=42)

# Step 5: Define ensemble (Voting Classifier)
voting = VotingClassifier(
    estimators=[
        ("rf", rf),
        ("xgb", xgb),
        ("lr", lr)
    ],
    voting="soft"
)

# Step 6: Model dictionary
models = {
    "Random Forest": rf,
    "XGBoost": xgb,
    "AdaBoost": ada,
    "Voting Classifier": voting
}

# Step 7: Train and evaluate all models
for name, model in models.items():
    print(f"\n{'='*20} {name} {'='*20}")
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, preds))
    
    print("\nClassification Report:")
    print(classification_report(y_test, preds))
