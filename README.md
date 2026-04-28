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

### 1. Weather is okay - Positive (Expected: Neutral)
This misclassification occurs because the word “okay” has a slightly positive score in the VADER lexicon. Since VADER is rule-based, it evaluates sentiment using individual word scores rather than full context. As a result, mildly positive words can push the overall compound score into the positive range. However, in human interpretation, “weather is okay” is generally neutral. This highlights a limitation of lexicon-based models in handling subtle or context-dependent meanings.
### 2. 111 - Invalid input
The input “111” is correctly rejected because it contains no alphabetic characters. The validation layer filters such inputs before sentiment analysis, ensuring only meaningful text is processed. This prevents non-linguistic data from being analyzed. However, it also shows that the system relies on rule-based validation rather than understanding whether the input is semantically meaningful language.
