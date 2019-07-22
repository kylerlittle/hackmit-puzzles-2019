
# each location has only a zip code; likewise,
# each of the first three notes of each recording are distinct
# this is the mapping to phone numbers

recordings = [
    {
        "notes": "D C# Eb B F B A Bb C D",
        "location": "fort smith",
        "zipcode": "479"
    },
    {
        "notes": "C B Eb A Bb B Eb A C# C",
        "location": "syracuse",
        "zipcode": "315"
    },
    {
        "notes": "Bb F A D A C# A C B C",
        "location": "idaho",
        "zipcode": "208"
    }
]

def phone_format(n: str) -> str:
    """Return formatted phone string
    """
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]   

# create mapping
mapping = {}

for recording in recordings:
    # take first three notes and map them to the digits
    for i, note in enumerate(recording['notes'].split(" ")[:3]):
        mapping[note] = recording['zipcode'][i]

# output phones numbers to call
for recording in recordings:
    phone_number = "".join(
        map(lambda note: mapping[note], recording['notes'].split(" "))
    )
    print("Try calling {}".format(phone_format(phone_number)))