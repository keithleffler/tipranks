
class Portfolio():
    def __init__(self, client):
        self.client = client

    def get_portfolio(self):
        return self.client.request(
            method="GET",
            endpoint='/api/v2/portfolio'
        )
