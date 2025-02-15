from enum import Enum

class ScreenerTipRanksScore(Enum):
    out_perform = 5
    above_avg = 4
    avg = 3
    below_avg = 2
    under_perform = 1

class ScreenerTargetUpside(Enum):
    up_gt20 = 8
    up_10_to_20 = 7
    up_5_to_10 = 6
    up_0_to_5 = 5
    down_0_to_5 = 4
    down_5_to_10 = 3
    down_10_to_20 = 2
    down_gt20 = 1

class ScreenerSortBy(Enum):
    aum = 1
    upside = 3
    analyst_consensus =5
    name = 16
    smart_score = 20
    holdings_count = 59

class ScreenerSortBy(Enum):
    ascending = 1
    descending = 2
