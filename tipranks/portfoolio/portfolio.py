from tipranks.client import TrClient


class Portfolio():
    def __init__(self, client:TrClient):
        self.client = client

    def get_portfolio(self):
        return self.client.request(
            method="GET",
            endpoint='/api/v2/portfolio'
        )
