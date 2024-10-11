import requests
from datetime import datetime, timedelta

def fetch_latest_news(api_key, news_keywords, lookback_days=10):
    if not news_keywords or not all(keyword.isalpha() for keyword in news_keywords):
        raise ValueError("Invalid news keywords")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=lookback_days)
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': ' OR '.join(news_keywords),
        'from': start_date.strftime('%Y-%m-%d'),
        'to': end_date.strftime('%Y-%m-%d'),
        'language': 'en',
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    articles = response.json().get('articles', [])
    return articles
