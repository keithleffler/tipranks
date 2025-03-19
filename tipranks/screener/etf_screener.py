from tipranks.client import TrClient
from .enums import *
class ETFParams():

    def __init__(self):
        self.sortBy = SortBy.smart_score.value
        self.sortDir = SortDir.descending.value
        self.page = 1
        self.pageSize = 50
        self.country = "us"
        self.method = "screenerStocks"
        # self.tipranksScore = ScoreCategory.out_perform #[ScoreCategory.out_perform.value,ScoreCategory.above_avg.value]
        self.assetClass = "Equity"
        self.type="GetStocks"
        # self.exchange = ["xnas","xnys","arcx","xase","bats"]

    @property
    def screenerParams(self):
        params = self.__dict__
        # params['tipranksScore[]'] = self.tipranksScore
        params['tipranksScore[]'] = [ScoreCategory.out_perform.value,ScoreCategory.above_avg.value]
        params['exchange[]'] = ["xnas","xnys","arcx","xase","bats"]
        return params

class EtfScreener():
    def __init__(self, client: TrClient):
        self.client = client

    def screen(self,params:ETFParams):
        screenerParams = params.screenerParams
        return self.client.request(
            method='GET',
            endpoint="/api/etfs/screener",
            params=screenerParams
        )

    def top_smart_score(self):
        pass

    def top_upside_potential(self):
        pass

