import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

    seen = set()
    new_data = []
    duplicate = 0
    for record in data:
        if record["objectid"] not in seen:
            seen.add(record["objectid"])
            new_data.append(record)
        else:
            duplicate += 1
    print(duplicate)
    data = new_data

    count = 0
    for record in data:
        # print(max(record["prediction"]))
        if max(record["prediction"]) > .999:
            count += 1
    print(count/len(data))
    print(len(data))

    sorted_data = sorted(data, key= lambda record : max(record["prediction"]), reverse=True)

    thing = [record for record in data if max(record["prediction"]) > .999]
    counts = [(0,0)] * 100
    for i in range(100):
        counts[i][0] = i
        for record in thing:
            if record["prediction"][i] > .999:
                counts[i][1] += 1


    for _class, _ in sorted(counts, key=lambda tup : tup[1], reverse=True)
    print(counts)

    # counts = [0] * 100
    totals = [0] * 100
    for i in range(100):
        for record in data:
            # counts[i] += 1
            totals[i] += record["prediction"][i]
        totals[i] = totals[i] / len(data)
    print(totals)

        

with open("data.csv", "w") as output:
    output.write(",".join(list(map(lambda record : record["objectid"], sorted_data))[:1000]))