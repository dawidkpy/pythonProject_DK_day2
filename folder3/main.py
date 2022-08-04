
import csv
import json

slownik = []

with open("my_csv.csv", encoding="utf-8") as file:
    moj_csv = csv.DictReader(file)

    for r in moj_csv:
        slownik.append(r)

print(slownik)

with open("my_json.json", "w", encoding="utf-8") as file2:
    file2.write(json.dumps(slownik, indent=4))
    #file2.write(json.dumps(slownik))

