import json
import asyncio
import numpy as np
from websockets.asyncio.client import connect


async def main(data: list):
    async with connect("ws://localhost:12345") as websocket:
        async for message in websocket:
            data.append(json.loads(message)["value"])
            arr = np.array(data)
            print(f"mean: {np.mean(arr)} and std: {np.std(arr)}")


if __name__ == "__main__":
    data = list()
    asyncio.run(main(data))
