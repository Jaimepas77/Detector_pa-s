import json, requests
from unicodedata import normalize
"""This code tells you if you can form a country name with the given characters."""

countries_file = "countries.json"

# countries = json.load(open(countries_file))    #Load json to dict (https://gist.github.com/Yizack/bbfce31e0217a3689c8d961a356cb10d)
countries = json.loads(requests.get("https://gist.githubusercontent.com/Yizack/bbfce31e0217a3689c8d961a356cb10d/raw/2e18fbfeb65d9c75f396a3a22934112b6ae2472c/countries.json").text)

while True:
    #Get a set of the spanish standar names as a set of letters
    trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)  #From https://es.stackoverflow.com/a/135736

    normalized = [x.get("name_es").upper() for x in countries.get("countries")]
    normalized = set([normalize('NFKC', normalize('NFKD', s).translate(trans_tab)) for s in normalized])

    #Get the characters of the country to be guessed
    guess = input("Introduce las letras del país: ").upper()
    sol = [x for x in normalized if set(guess).issuperset(set(x))]    #Get the countries that use the same characters

    tmp = list()    #Checking that a character isn't used more times than the allowed ones
    for x in sol:
        accept = True
        for c in guess:
            if guess.count(c) < x.count(c):
                accept = False
                break
        if(accept):
            tmp.append(x)
    sol = list(set(tmp))

    print(f"Los países que encajan son {sol}")

    answer = input("¿Otra vez? (s/n): ")
    if(answer.lower() == "n"):
        break

    #print(normalized)
