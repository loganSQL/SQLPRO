# https://medium.com/@jialun.tom.chen/using-python-async-await-to-get-your-data-fast-fe6d9ce7c6e

import requests
import json
import pandas as pd
#import config

def get_json(symbol,api_key):
  payload = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': symbol,
    'outputsize': 'full',
    #'apikey': config.ALPHA_API_KEY,
    'apikey': api_key,
    # AA api default data type is json, another option is csv
    'datatype': 'json'
  }
  r = requests.get('https://www.alphavantage.co/query?', params=payload)
  data = json.loads(r.text)['Time Series (Daily)']
  with open(f'./data/data_{symbol}.json', 'w') as outfile:
    json.dump(data, outfile)

if __name__ == '__main__':
  api_key="XXXXXX"
  get_json('ROKU',api_key)
  get_json('MSFT',api_key)