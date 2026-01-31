import asyncio, time
from telegram import Bot
from config import *
from market import fetch_ohlcv, is_liquid
from strategy import liquidity_sweep_signal
from risk import spot_targets

bot = Bot(token=TELEGRAM_TOKEN)
cooldowns = {}

async def send_signal(symbol, price):
    t = spot_targets(price)
    msg = f"""
📢 SIGNAL SCALPING SPOT
🪙 {symbol}
⏱ TF : {TIMEFRAME}

🟢 Entrée : {price}
🛑 Stop : {t['sl']}
🎯 TP1 : {t['tp1']}
🎯 TP2 : VWAP

⚠️ Discipline obligatoire
"""
    await bot.send_message(chat_id=CHAT_ID, text=msg)

async def scan():
    while True:
        for s in SYMBOLS:
            if not is_liquid(s):
                continue

            if s in cooldowns and time.time() - cooldowns[s] < COOLDOWN_MINUTES * 60:
                continue

            df = fetch_ohlcv(s, TIMEFRAME)
            if liquidity_sweep_signal(df):
                price = df["close"].iloc[-1]
                await send_signal(s, price)
                cooldowns[s] = time.time()

        await asyncio.sleep(30)

asyncio.run(scan())
