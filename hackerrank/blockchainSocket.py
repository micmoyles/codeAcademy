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
        first_message = json.dumps({"op":"unconfirmed_sub"})
        yield from websocket.send(first_message)
        print("> {}".format(first_message))

        greeting = yield from websocket.recv()
        print("< {}".format(greeting))

    finally:
        yield from websocket.close()

asyncio.get_event_loop().run_until_complete(hello())

def subscribe():
    websocket = yield from websockets.connect(
        'wss://ws.blockchain.info/inv')
    sub_message = json.dumps({"op": "ping"})
    print("> {}".format(sub_message))
    yield from websocket.send(sub_message)
    resp = yield from websocket.recv()
    print("< {}".format(resp))

subscribe()