import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

TIMEFRAME = "1m"

SYMBOLS = [
    "PEPE/USDT",
    "DOGE/USDT",
    "SHIB/USDT"
]

MIN_VOLUME_USDT = 5_000_000
COOLDOWN_MINUTES = 10
