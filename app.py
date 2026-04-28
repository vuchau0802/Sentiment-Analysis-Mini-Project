from flask import Flask, request, jsonify, render_template
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    if not isinstance(text, str):
        return {"error": "text must be string"}

    if text.strip() == "":
        return {"error": "text cannot be empty"}

    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "text": text,
        "sentiment": sentiment,
        "compound_score": round(compound, 3)
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        text = request.form.get('text')
        result = analyze_sentiment(text)

    return render_template("index.html", result=result)

@app.route('/sentiment', methods=['GET', 'POST'])
def get_sentiment():
    if request.method == 'GET':
        text = request.args.get('text')
    else:
        data = request.get_json()
        text = data.get('text') if data else None

    if not text:
        return jsonify({"error": "Missing text"}), 400

    result = analyze_sentiment(text)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)