"""
stock_sentiment_nlu — Stock sentiment analysis using NLU.

Provides analyzers and utility functions for extracting sentiment
from financial news headlines and articles.
"""

from .analyzer import SentimentAnalyzer
from .utils import fetch_news_headlines, clean_text

__all__ = ["SentimentAnalyzer", "fetch_news_headlines", "clean_text"]
__version__ = "0.1.0"
