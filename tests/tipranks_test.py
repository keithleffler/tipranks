import unittest
import boto3

from tipranks import TipRanks


class MyTestCase(unittest.TestCase):
    client = None
    def setUp(self):
        if not(self.client):
            ssm_client = boto3.client('ssm')
            email = ssm_client.get_parameter(Name='/side-hustle/tipranks/email')['Parameter']['Value']
            password = ssm_client.get_parameter(Name='/side-hustle/tipranks/password', WithDecryption=True)['Parameter'][
                'Value']
            try:
                self.client = TipRanks(email=email, password=password)
            except Exception as err:
                pass

    def test_get_top_analyst_stocks(self):
        self.client.get_top_analyst_stocks()

    def test_get_top_smart_score_stocks(self):
        self.client.get_top_smart_score_stocks()

    def test_get_top_insider_stocks(self):
        self.client.get_top_insider_stocks()

    def test_get_stock_screener(self):
        self.client.get_stock_screener()

    def test_get_top_online_growth_stocks(self):
        self.client.get_top_online_growth_stocks()

    def test_get_trending_stocks(self):
        self.client.get_trending_stocks()

    def test_get_top_experts(self):
        self.client.get_top_experts('analyst')

    def test_get_analyst_projection(self):
        self.client.get_analyst_projection('aapl')

    def test_get_news_sentiment(self):
        self.client.get_news_sentiment('aapl')

    def test_get_portfolio(self):
        portfolio = self.client.get_portfolio()
        pass


if __name__ == '__main__':
    unittest.main()
