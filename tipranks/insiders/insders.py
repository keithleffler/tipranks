from tipranks.client import TrClient

import time


class Insiders():
    def __init__(self, client: TrClient):
        self.client = client

    def get_top_insider_stocks(self) -> list:
        return self.__request(
            method="GET",
            endpoint="/api/insiders/getTrendingStocks/",
            params={
                "benchmark": "1",
                "period": "3",
                "country": "US",
                "break": int(time.time())
            }
        )
