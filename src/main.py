import time
from config import nomics_token, telegram_token
from src.api_nomics.ticker import Ticker
from src.bot_telegram.bot_alerter import BotAlerter
from src.bot_telegram.bot_telegram import BotTelegram
ticker = Ticker(nomics_token)
bot = BotTelegram(telegram_token)
alerter = BotAlerter()
bot.answer_message_with(alerter.add_alert)

while True:
    alerter.alert_system.update_exchange(ticker.get_prices('BTC, ETH'))
    for currency in alerter.alert_system.exchange.currencies:
        print(currency.symbol, currency.price)
    time.sleep(30)

