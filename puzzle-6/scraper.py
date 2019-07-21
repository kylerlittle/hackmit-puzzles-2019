import requests
import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)


for i in range(1000):
    x = requests.get('https://partition.hackvengers.dev/api/Zackh1998_2edfda/prediction')

    data.append(x.json())

    if i % 10 == 0:
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)

