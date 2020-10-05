import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        user_resp = input("Did you mean %s ? Enter Y if Yes, or N if No. " % get_close_matches(w, data.keys())[0])
        if user_resp == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif user_resp == "N":
            return "The word doesn't exist. Please double check it."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the word: ")

output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


