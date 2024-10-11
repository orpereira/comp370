import unittest
from newscover.newsapi import fetch_latest_news
import json

class TestFetchLatestNews(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('newscover/tests/test_secrets.json') as f:
            cls.api_key = json.load(f)['api_key']

    def test_no_news_keywords(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, [])

    def test_lookback_days(self):
        articles = fetch_latest_news(self.api_key, ['test'], lookback_days=1)
        for article in articles:
            published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertGreaterEqual(published_at, datetime.now() - timedelta(days=1))

    def test_invalid_keyword(self):
        with self.assertRaises(ValueError):
            fetch_latest_news(self.api_key, ['test123'])

if __name__ == '__main__':
    unittest.main()