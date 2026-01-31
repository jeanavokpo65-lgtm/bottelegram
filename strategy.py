def ema(series, p):
    return series.ewm(span=p).mean()

def compute_vwap(df):
    return (df["close"] * df["volume"]).cumsum() / df["volume"].cumsum()

def liquidity_sweep_signal(df):
    df["ema9"] = ema(df["close"], 9)
    df["ema21"] = ema(df["close"], 21)
    df["vwap"] = compute_vwap(df)

    last = df.iloc[-1]
    low = df["low"].iloc[-10:-1].min()

    return (
        last["low"] < low and
        last["close"] > low and
        last["volume"] > df["volume"].iloc[-10:-1].mean() * 1.5 and
        last["ema9"] > last["ema21"] and
        last["close"] < last["vwap"]
    )
