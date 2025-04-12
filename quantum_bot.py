import os
from binance.client import Client
from dotenv import load_dotenv
import time, ta

load_dotenv()
client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET_KEY"))

def get_balance():
    balances = client.futures_account_balance()
    for b in balances:
        if b['asset'] == 'USDT':
            return float(b['balance'])
    return 0

def open_trade(symbol, side, qty):
    try:
        client.futures_create_order(
            symbol=symbol, 
            side=side, 
            type='MARKET', 
            quantity=qty
        )
    except Exception as e:
        print(e)

# Loop principal (simplificado, completo na implantação)
while True:
    saldo = get_balance()
    if saldo > 20:
        qty = saldo * 0.02
        open_trade("BTCUSDT", "BUY", qty)
    time.sleep(60)
