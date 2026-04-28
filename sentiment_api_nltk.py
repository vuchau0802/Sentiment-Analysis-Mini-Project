from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import re

# Download lexicon only if not already installed
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    
    if not isinstance(text, str):
        return {"error": "text must be string"}
    text = text.strip()

    if not text:
        return {"error": "Invalid input: text cannot be empty"}
    if not re.search(r"[a-zA-Z]", text):
        return {"error": "Invalid input: text must contain alphabetic characters"}

    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    readable_scores = {
    "positive": round(scores["pos"], 3),
    "negative": round(scores["neg"], 3),
    "neutral": round(scores["neu"], 3),
    "compound": round(scores["compound"], 3)
    }

    return {
        "text": text,
        "sentiment": sentiment,
        "compound_score": round(compound, 3),
        "scores": readable_scores
    }

if __name__ == "__main__":
    test_cases = [

        ("I love this product", "Positive"),
        ("Amazing experience", "Positive"),
        ("Best decision ever", "Positive"),
        ("Service was excellent", "Positive"),

        ("I hate you", "Negative"),
        ("Very bad experience", "Negative"),
        ("Worst ever", "Negative"),
        ("This is terrible", "Negative"),

        ("The meeting is at 3 PM", "Neutral"),
        ("I went to the store", "Neutral"),
        ("This is a book", "Neutral"),
        ("Weather is okay", "Neutral"),

        ("111", "Invalid"),
        ("", "Invalid"),
    ]

    print("\n==== Analysis Results ====\n")

    for text, expected in test_cases:
        result = analyze_sentiment(text)

        if "error" in result:
            print(f"INPUT: {text}")
            print(f"ERROR: {result['error']}\n")
        else:
            print(f"INPUT: {result['text']}")
            print(f"SENTIMENT: {result['sentiment']}")
            print(f"SCORE: {result['scores']}\n")

    print("\n====REPORT TABLE ====\n")

    print(f"{'INPUT':30} | {'EXPECTED':10} | {'PREDICTED':10} | RESULT")
    print("-" * 75)

    correct = 0

    for text, expected in test_cases:
        result = analyze_sentiment(text)

        if "error" in result:
            predicted = "Invalid"
        else:
            predicted = result["sentiment"]

        status = "PASS" if predicted == expected else "FAIL"

        if status == "PASS":
            correct += 1

        display_text = text if text.strip() else "[EMPTY]"

        print(f"{display_text[:30]:30} | {expected:10} | {predicted:10} | {status}")

    accuracy = correct / len(test_cases)

    print("\n" + "-" * 75)
    print(f"Accuracy: {round(accuracy * 100, 2)}%")