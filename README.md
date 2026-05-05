# AI Data Engine: Text Safety Evaluation

## Key Insight (What Actually Matters for AI Systems)

Model performance was not limited by the model.

Moderate inter-annotator agreement (Cohen’s Kappa ~0.4–0.5) revealed that inconsistent labeling was the primary constraint on performance.

Improving annotation quality would yield greater gains than model tuning.

---

## Overview

This project simulates an AI data engine for sensitive text classification in safety-critical systems.

It demonstrates how data quality, annotation consistency, and evaluation pipelines directly impact model performance.

---

## Data Engine Thinking

This project models a real-world ML pipeline:

Raw Data → Annotation → QA → Adjudication → Evaluation → Iteration

Key focus:
- identifying failure modes (false positives / false negatives)
- improving dataset quality instead of model complexity
- reducing ambiguity in labeling systems

---

## Failure Modes Identified

- False positives caused by ambiguous phrasing  
- False negatives due to unclear labeling rules  
- Moderate annotator disagreement (Kappa ~0.4–0.5)  

These indicate data quality—not model architecture—was the limiting factor.

---

## Results

- Precision: 0.84  
- Recall: 0.89  
- F1 Score: 0.866  
- Accuracy: 0.87  

---

## Confusion Matrix

![Confusion Matrix](outputs/confusion_matrix_visual.png)

---

## System Impact

This project demonstrates that:

- Data quality is the primary driver of model performance  
- Annotation consistency is critical for scaling ML systems  
- Evaluation frameworks must identify root causes, not just metrics  

---

## How to Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/run_model_evaluation.py
