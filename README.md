

## Usage

The script makes use of bitfinex, installation is required.

```bash
pip install -r requirements.txt
python main.py
```

In real-time trading, order books are very important data, and we need to keep a snapshot of order book at local ram. Bitfinex(https://www.bitfinex.com/) is one of biggest cryptocurrency exchanges. This is a program to update the given symbol’s orderbook from exchange using its WebSocket API. In this project, I am booking the following symbol BTC_USDT, EOS_BTC, STORJ_BTC.
