import nomics
import time
from src.crypto.alert_system import CryptoPriceAlertSystem
nomic = nomics.Nomics('***REMOVED***')
alert_system = CryptoPriceAlertSystem()
alert_system.add_alert('BTC', 30_000, lambda: print('Paso los 30k'))

while True:
    updates = {'BTC':{ 'price': float(nomic.Currencies.get_currencies(ids='BTC, ETH', interval='1h')[0]['price'])}}
    print(updates)

    alert_system.update_exchange(updates)
    time.sleep(1)

