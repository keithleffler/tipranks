from tipranks.client import TrClient
import time


class Experts():
    def __init__(self, client: TrClient):
        self.client = client

    def get_top_experts(self, expert_type: str) -> list:
        # expertType ="analyst"
        # numExperts = <number>
        # period = "month","quarter","year","twoYears"
        # benchmark = "none", "snp500","sector"
        # sector: "Services","Industrialgoods","consumergoods","Utilities","Healthcare","Materials","Technology","Financial"
        # country = "us"

        if expert_type.lower() == "analyst":
            params = {
                "expertType": "analyst",
                "numExperts": "100",
                "period": "year",
                "benchmark": "none"
            }
        else:
            params = {
                "expertType": expert_type,
                "numExperts": "100"
            }

        return self.__request(
            method="GET",
            endpoint="/api/experts/GetTop25Experts/",
            params=params
        )
