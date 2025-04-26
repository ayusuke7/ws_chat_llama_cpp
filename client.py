import asyncio

import websockets


async def chat():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = input("Você: ")
            await websocket.send(msg)
            resposta = await websocket.recv()
            print(f"LLM: {resposta}")

asyncio.run(chat())
