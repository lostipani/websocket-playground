import json
import asyncio
from websockets.asyncio.client import connect


async def main(data: list):
    async with connect("ws://localhost:12345") as websocket:
        async for message in websocket:
            data.append(json.loads(message)["value"])
            print(data)


if __name__ == "__main__":
    data = []
    asyncio.run(main(data))
