from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "positive 😊"
    elif sentiment < 0:
        return "negative 😡"
    else:
        return "neutral 😐"

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)['compound']

    if sentiment > 0.05:
        return "positive😊"
    elif sentiment < -0.05:
        return "negative😡"
    else:
        return "neutral😐"

def analyze_input():
    text = input("Enter a sentence for sentiment analysis: ")
    print(f"TextBlob Sentiment: {analyze_sentment_textblob(text)}")
    print(f"Vader Sentiment: {analyze_sentiment_vader(text)}")
# Run the function
analyze_input()