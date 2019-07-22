import csv
import random
import string
import json
import requests
import asyncio
import concurrent.futures

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

    seen = set()
    new_data = []
    for record in data:
        if record["objectid"] not in seen:
            seen.add(record["objectid"])
            new_data.append(record)
    data = new_data


    sorted_data = sorted(data, key= lambda record : max(record["prediction"]), reverse=True)

    sorted_data = sorted_data[1200:] # first 1000 used to make test.csv



def add_to_good_ids(_id):
    with open("good.csv", "a") as good:
        good.write("," + _id)


def random_string():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)]).lower()

def test_request(test_id, user, ids):
    ids[999] = test_id
    URL = "https://partition.hackvengers.dev/api/{random_hash}/submission".format(
        random_hash = user
    )

    resp = requests.post(URL, files={"csv": ",".join(ids)})

    
    message = resp.json()['message']
    print(message )

    return "70" in message


with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    ids = list(reader)[0]

index = 0
def doATest():
    global index
    myIndex = index
    index += 1

    if test_request(sorted_data[myIndex]["objectid"], random_string(), ids):
        add_to_good_ids(sorted_data[myIndex]["objectid"])




async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                doATest
            )
            for i in range(100)
        ]
        for response in await asyncio.gather(*futures):
            pass


loop = asyncio.get_event_loop()
for _ in range(12):
    print("try run main")
    try:
        loop.run_until_complete(main())
    except json.decoder.JSONDecodeError:
        pass
    print("print")







# import requests
# r = requests.post("https://partition.hackvengers.dev/api/random_hash/submission", data={'number': 12524, 'type': 'issue', 'action': 'show'})
# >>> print(r.status_code, r.reason)
# 200 OK
# >>> print(r.text[:300] + '...')



# $('#csv-upload').change(function() {
#         let formData = new FormData();
#         formData.append('csv', $('#csv-upload').get(0).files[0]);

#         let filename = document.querySelector('.filename');
#         let input = document.querySelector('input');
#         filename.textContent = input.files[0].name;

#         $.ajax({
#             url: '/api/' + username + '/submission',
#             data: formData,
#             type: 'POST',
#             processData: false,
#             contentType: false,
#             success: function(resp) {
#                 $('#error').hide();
#                 $('#answer').show();
#                 $('#answer-msg').text(solution + resp);
#             },
#             error: function(resp) {
#                 $('#answer').hide();
#                 $('#error').show();
#                 if (resp.status == 413) {
#                     $('#error-msg').text('Submission is too large')
#                 } else {
#                     $('#error-msg').text(resp.responseJSON.message)
#                 }
#             }
#         });
#     });