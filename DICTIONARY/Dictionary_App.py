import json
from difflib import get_close_matches

data=json.load(open("076 data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no!!" % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            print("The word doesnt exist!")
        else:
            print("We didnt understad your query")

    else:
        print("The word doesnt exist!!!..Please recheck")

word=input("Enter Word:")

output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)