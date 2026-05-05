# AI Data Quality & Model Evaluation System
Sensitive Text Classification (Safety-Critical AI)

## Overview
This project demonstrates an end-to-end AI data quality system for sensitive text classification. It simulates how training data, annotation consistency, and evaluation pipelines directly impact model performance.

## Problem
Model performance in safety-critical systems is often limited not by model architecture, but by inconsistent or ambiguous training data.

This project focuses on identifying and solving that bottleneck.

## System Design
- Built dataset (100 labeled samples)
- Designed annotation guidelines and ontology
- Defined edge-case handling rules
- Implemented adjudication workflow
- Simulated multi-annotator labeling
- Evaluated model performance using standard ML metrics

## Results
- Precision: 0.84
- Recall: 0.89
- F1 Score: 0.866
- Accuracy: 0.87

## Key Insight
Moderate inter-annotator agreement (Cohen’s Kappa ~0.4–0.5) revealed that labeling inconsistency—not model capability—was the primary constraint on performance.

## Why This Matters
Improving annotation quality and reducing ambiguity is often the highest-leverage way to improve AI systems.

## Project Structure

## Confusion Matrix
![Confusion Matrix](outputs/confusion_matrix_visual.png)
