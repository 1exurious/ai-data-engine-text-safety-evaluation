"""
FSD Text Safety Classifier Evaluation
Dummy portfolio project generated for AI Data Quality / Model Evaluation practice.

How to run:
1. Install dependencies:
   pip install pandas scikit-learn matplotlib openpyxl
2. Put raw_dataset_100_records.csv in the same folder as this script.
3. Run:
   python run_model_evaluation.py
4. Outputs:
   - printed classification metrics
   - confusion_matrix_visual.png
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score, ConfusionMatrixDisplay, cohen_kappa_score

DATA_PATH = "raw_dataset_100_records.csv"
POS_LABEL = "SENSITIVE"
NEG_LABEL = "NON_SENSITIVE"

# Load the raw human-gold-labeled dataset.
df = pd.read_csv(DATA_PATH)

# Convert labels into binary values for sklearn metrics.
# 1 = Sensitive, 0 = Non-sensitive.
y_true = (df["actual_label"] == POS_LABEL).astype(int)
y_pred = (df["model_prediction"] == POS_LABEL).astype(int)

# Confusion matrix layout: [[TN, FP], [FN, TP]] in sklearn default binary order [0,1].
cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
tn, fp, fn, tp = cm.ravel()

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
accuracy = accuracy_score(y_true, y_pred)

print("=== FSD Text Safety Classifier Evaluation ===")
print(f"True positives: {tp}")
print(f"False positives: {fp}")
print(f"False negatives: {fn}")
print(f"True negatives: {tn}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1: {f1:.3f}")
print(f"Accuracy: {accuracy:.3f}")

# Inter-annotator agreement: Cohen's Kappa for reviewer pairs.
reviewers = ["annotator_lex", "annotator_maya", "annotator_rafael"]
for i in range(len(reviewers)):
    for j in range(i + 1, len(reviewers)):
        kappa = cohen_kappa_score(df[reviewers[i]], df[reviewers[j]])
        print(f"Cohen kappa {reviewers[i]} vs {reviewers[j]}: {kappa:.3f}")

# Visualize confusion matrix.
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[NEG_LABEL, POS_LABEL]
)
display.plot(values_format="d")
plt.title("Confusion Matrix - Sensitive Text Classifier")
plt.tight_layout()
plt.savefig("confusion_matrix_visual.png", dpi=200)
print("Saved confusion_matrix_visual.png")
