from tipranks.client import TrClient
import time


class Stocks():
    def __init__(self, client: TrClient):
        self.client = client

    def get_news_sentiment(self, ticker: str) -> list:
        return self.client.request(
            method="GET",
            endpoint="/api/stocks/getNews/",
            params={
                "ticker": ticker
            }
        )

    def get_top_analyst_stocks(self) -> list:
        return self.client.request(
            method="GET",
            endpoint="/api/stocks/getMostRecommendedStocks/",
            params={
                "benchmark": "1",
                "period": "3",
                "country": "US",
                "break": int(time.time())
            }
        )

    def get_trending_stocks(self) -> list:
        return self.__request(
            method="GET",
            endpoint="/api/stocks/gettrendingstocks/",
            params={
                "daysago": "30",
                "which": "most",
                "country": "us",
                "break": int(time.time())
            }
        )
