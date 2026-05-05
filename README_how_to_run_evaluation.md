# How to Run the Actual Evaluation in Python

## Files
- `raw_dataset_100_records.csv`: raw dummy dataset
- `raw_dataset_100_records.xlsx`: formatted analyst workbook
- `run_model_evaluation.py`: Python evaluation script
- `confusion_matrix_visual.png`: generated visual example
- `inter_annotator_agreement_report.docx`: analyst-style IAA report

## Step 1: Install Python dependencies
```bash
pip install pandas scikit-learn matplotlib openpyxl
```

## Step 2: Run the script
Put `run_model_evaluation.py` and `raw_dataset_100_records.csv` in the same folder, then run:

```bash
python run_model_evaluation.py
```

## What a confusion matrix is
A confusion matrix is a 2x2 error table that shows how model predictions compare to the gold labels.

For sensitive-text detection:

| Outcome | Meaning |
|---|---|
| True Positive | Sensitive text correctly flagged sensitive |
| False Positive | Non-sensitive text incorrectly flagged sensitive |
| False Negative | Sensitive text incorrectly missed |
| True Negative | Non-sensitive text correctly passed |

## Project metrics from this dummy dataset
- TP: 42
- FP: 8
- FN: 5
- TN: 45
- Precision: 0.840
- Recall: 0.894
- F1: 0.866
- Accuracy: 0.870

## Precision / recall tradeoff
Precision answers: when the model flags text as sensitive, how often is it right?
Recall answers: out of all truly sensitive text, how much did the model catch?

For a safety classifier, recall is usually weighted more heavily because missed sensitive content can create privacy, safety, or compliance risk. False positives still matter, but they usually cause friction rather than direct exposure.
