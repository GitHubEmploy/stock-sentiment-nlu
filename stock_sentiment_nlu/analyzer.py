"""
NLU-based sentiment analysis for stock market news.

Uses NLTK's VADER lexicon (a rule-based sentiment model tuned for
social media / financial text) to classify news headlines as
positive, negative, or neutral.
"""

from typing import Dict, List, Union
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    """
    Sentiment analyzer for stock market news headlines.

    Uses VADER (Valence Aware Dictionary and sEntiment Reasoner),
    a lexicon and rule-based sentiment analysis tool specifically
    attuned to sentiments expressed in social media and financial text.
    """

    def __init__(self):
        try:
            self._sia = SentimentIntensityAnalyzer()
        except LookupError:
            nltk.download("vader_lexicon", quiet=True)
            self._sia = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> Dict[str, float]:
        """
        Analyze sentiment of a single text string.

        Returns a dict with keys: 'neg', 'neu', 'pos', 'compound'
        where 'compound' is the normalized sentiment score (-1 to 1).
        """
        return self._sia.polarity_scores(text)

    def analyze_batch(self, texts: List[str]) -> List[Dict[str, float]]:
        """Analyze sentiment for a list of text strings."""
        return [self.analyze(t) for t in texts]

    def classify(self, text: str) -> str:
        """
        Classify text as 'positive', 'negative', or 'neutral'
        based on the compound score.
        """
        scores = self.analyze(text)
        compound = scores["compound"]
        if compound >= 0.05:
            return "positive"
        elif compound <= -0.05:
            return "negative"
        return "neutral"

    def score(self, text: str) -> float:
        """Return the compound sentiment score (-1 to 1)."""
        return self.analyze(text)["compound"]


if __name__ == "__main__":
    analyzer = SentimentAnalyzer()

    headlines = [
        "Apple reports record quarterly earnings, stock surges",
        "Trade war fears escalate as tariffs take effect",
        "Company announces new product line expansion",
        "FDA rejects new drug application, shares plummet",
    ]

    print(f"{'Headline':<60} {'Score':>7} {'Sentiment'}")
    print("-" * 80)
    for h in headlines:
        s = analyzer.score(h)
        c = analyzer.classify(h)
        print(f"{h:<60} {s:>7.3f} {c}")
