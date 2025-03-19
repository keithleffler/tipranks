
import time
class StockScreener():
    def __init__(self, client):
        self.client = client

    def get_top_smart_score_stocks(self) -> list:
        return self.client.request(
            method="GET",
            endpoint="/api/Screener/GetStocks/",
            params={
                "break": int(time.time()),
                "country": "US",
                "page": "1",
                "sortBy": "1",
                "sortDir": "2",
                "tipranksScore": "5"
            }
        )

    def get_stock_screener(self) -> list:
            return self.__request(
                method="GET",
                endpoint="/api/Screener/GetStocks/",
                params = {
                    "break": int(time.time()),
                    "country": "US",
                    "page": "1",
                    "sortBy": "1",
                    "sortDir": "2",
                }
            )

    def get_top_online_growth_stocks(self) -> list:
        return self.__request(
            method="GET",
            endpoint="/api/websiteTraffic/screener",
            params={
                "country": "us"
            }
        )
