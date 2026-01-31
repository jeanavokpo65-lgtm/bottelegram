import ccxt, pandas as pd

exchange = ccxt.binance({
    "enableRateLimit": True,
    "options": {"defaultType": "spot"}
})

def fetch_ohlcv(symbol, timeframe, limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    return pd.DataFrame(ohlcv, columns=[
        "time","open","high","low","close","volume"
    ])

def is_liquid(symbol):
    return exchange.fetch_ticker(symbol)["quoteVolume"] >= 5_000_000
