
import os

try:
    nomics_token = os.environ['NOMICS_TOKEN']
    telegram_token = os.environ['TELEGRAM_TOKEN']
    coin_mkt_token = os.environ['COIN_MKT_TOKEN']

except KeyError:
    nomics_token = ''
    telegram_token = ''

