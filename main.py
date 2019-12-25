import time
from bitfinex import WssClient


if __name__ == '__main__':
    def my_handler(message):
        # Print the result every iteration
        print(message)

    my_client = WssClient()

    my_client.subscribe_to_orderbook(
        symbol="BTCUSD",
        precision="P1",
        callback=my_handler
    )

    my_client.subscribe_to_orderbook(
        symbol="EOSBTC",
        precision="P1",
        callback=my_handler
    )

    my_client.subscribe_to_orderbook(
        symbol="STJBTC",
        precision="P1",
        callback=my_handler
    )

    my_client.start()

    time.sleep(2)