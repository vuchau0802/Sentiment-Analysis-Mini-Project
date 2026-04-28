# Sentiment Analysis Mini Project (NLTK + Flask)

## Overview
This project is a simple **Sentiment Analysis system** built using:
- Python
- NLTK (VADER sentiment model)
- Flask

It classifies text into:
- Positive
- Negative
- Neutral

------

## Error Analysis

### 1. Weather is okay → Positive (Expected: Neutral)
This misclassification occurs because the word “okay” carries a slight positive sentiment in VADER lexicon...

### 2. 111 → Invalid input
This input is correctly rejected because it does not contain alphabetic characters...
