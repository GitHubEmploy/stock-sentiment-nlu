"""
Utility functions for stock sentiment analysis.
"""

import re
from typing import List, Optional
import requests


def clean_text(text: str) -> str:
    """
    Clean and normalize text for sentiment analysis.

    - Lowercases the text
    - Removes URLs
    - Removes HTML tags
    - Strips extra whitespace
    """
    text = text.lower()
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_news_headlines(
    api_key: str,
    query: str = "stock market",
    count: int = 10,
) -> List[str]:
    """
    Fetch recent news headlines from NewsAPI.

    Args:
        api_key: NewsAPI API key
        query: Search query (e.g. 'AAPL', 'stock market')
        count: Number of headlines to fetch (max 100)

    Returns:
        List of headline strings
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "pageSize": min(count, 100),
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": api_key,
    }

    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    headlines = []
    for article in data.get("articles", []):
        title = article.get("title")
        if title:
            headlines.append(title)

    return headlines
