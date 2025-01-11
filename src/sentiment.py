import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer # type: ignore
from nltk import tokenize


def analyze(comment):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(comment)
    return sentiment

