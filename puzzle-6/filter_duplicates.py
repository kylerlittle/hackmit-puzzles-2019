import csv
import json

with open('good.csv', 'r') as f:
    reader = csv.reader(f)
    ids = list(reader)[0]

ids = list(set(ids))

with open("good.csv", 'w', newline='') as good:
     wr = csv.writer(good)
     wr.writerow(ids)


with open('good.csv', 'r') as file:
    data = file.read().replace('\n', '')

with open('good.csv', 'w') as file:
    file.write(data)


with open('good.csv', 'r') as f:
    reader = csv.reader(f)
    ids = list(reader)[0]

ids = list(set(ids))

print(len(ids))


with open('data.json', 'r') as json_file:
    data = json.load(json_file)

    seen = set()
    new_data = []
    for record in data:
        if record["objectid"] not in seen:
            seen.add(record["objectid"])
            new_data.append(record)
    data = new_data


    sorted_data = list(map(lambda record : record["objectid"], sorted(data, key= lambda record : max(record["prediction"]), reverse=True)))

    # sorted_data = sorted_data[1200:] # first 1000 used to make test.csv


data = ids + sorted_data

with open("mixed_data.csv", "w") as output:

    output_data = data[:1000]
    output.write(",".join(output_data))