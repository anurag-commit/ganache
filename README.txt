=============================
Blockchain Attack Detection
Collaborative Learning Setup
=============================

This project simulates a decentralized approach to detecting attacks (e.g., Flood of Transactions) in a blockchain system using collaborative learning across multiple nodes.

---

📁 Data Files
------------

- training_data.csv        → Full dataset with labeled block features
- node1_data.csv           → Subset of training_data for Node 1
- node2_data.csv           → Subset of training_data for Node 2
- node3_data.csv           → Subset of training_data for Node 3

---

⚙️ Core Scripts
--------------

1. split_dataset.py
   → Splits the main dataset into 3 equal parts for Node 1, 2, and 3.

2. train_node_model.py
   → Trains an XGBoost model on a given node’s dataset and saves the model as a .pkl file.
   → Usage:
      python train_node_model.py --data node1_data.csv --out node1_model.pkl

3. evaluate_node_model.py
   → Evaluates a saved model (.pkl) using a hold-out split from its original dataset.
   → Shows confusion matrix, accuracy, and classification report.
   → Usage:
      python evaluate_node_model.py --model node1_model.pkl --data node1_data.csv

4. aggregate_models.py
   → Performs collaborative prediction using soft voting from all 3 models.
   → Evaluates performance using the same test set.
   → Prints metrics to console only.

5. collab_evaluate.py
   → Same as aggregate_models.py, but also saves the results to collab_results.txt.
   → Useful for keeping records.

6. shap_explain.py
   → Visualizes feature importance using SHAP for a given node’s model and data.
   → Usage:
      python shap_explain.py --model node1_model.pkl --data node1_data.csv

---

📊 Output Files
---------------

- node1_model.pkl / node2_model.pkl / node3_model.pkl  → Trained models per node
- collab_results.txt                                  → Evaluation summary of the collaborative system
- SHAP visualizations (from shap_explain.py)          → Feature importance plots per node

---

📌 Summary
----------
This system simulates a collaborative learning environment where each node trains locally and contributes to a joint decision via soft voting. No raw data is shared, preserving privacy while maintaining strong attack detection performance.

