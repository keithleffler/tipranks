import boto3
from tipranks import TrClient,EtfScreener,ETFParams
import pandas as pd

ssm_client = boto3.client('ssm')
email = ssm_client.get_parameter(Name = '/side-hustle/tipranks/email')['Parameter']['Value']
password = ssm_client.get_parameter(Name = '/side-hustle/tipranks/password',WithDecryption=True)['Parameter']['Value']
client = TrClient(email,password)

screener = EtfScreener(client)
params = ETFParams()
screenerParams = params.screenerParams

matches = screener.screen(params)

tickers = [data['ticker'] for data in matches['data']]
n = len(tickers)
index = list(range(n))
df_data = pd.DataFrame.from_records(matches['data'][0:n],index=list(range(n)))
df_extra = pd.DataFrame.from_records(matches['extraData'][0:n],index = list(range(n)))
pass
