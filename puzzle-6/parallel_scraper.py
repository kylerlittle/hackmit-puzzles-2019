import asyncio
import concurrent.futures
import requests
import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.get, 
                'https://partition.hackvengers.dev/api/Zackh1998_2edfda/prediction'
            )
            for i in range(50)
        ]
        for response in await asyncio.gather(*futures):
            data.append(response.json())

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)


loop = asyncio.get_event_loop()
for _ in range(5000):
    try:
        loop.run_until_complete(main())
    except json.decoder.JSONDecodeError:
        pass
    print("print")