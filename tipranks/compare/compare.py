from tipranks.client import TrClient
import time


class Compare():
    def __init__(self, client: TrClient):
        self.client = client

    def get_analyst_projection(self, ticker: str) -> list:
        return self.__request(
            method="GET",
            endpoint="/api/compare/analystRatings/tickers/",
            params={
                "tickers": ticker.lower()
            }
        )
