#!/usr/bin/python3

import asyncio
import websockets
import json

@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect(
        'wss://ws.blockchain.info/inv')

    try:
        #name = input("What's your name? ")
        first_message = b'{"op":"ping"}'
        first_message = json.dumps({"op":"ping"})
        yield from websocket.send(first_message)
        print("> {}".format(first_message))

        greeting = yield from websocket.recv()
        print("< {}".format(greeting))

    finally:
        yield from websocket.close()

asyncio.get_event_loop().run_until_complete(hello())