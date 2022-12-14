
import csv
import json

def f_read(t_dict):

    with open("my_csv.csv", encoding="utf-8") as file:
        t_csv = csv.DictReader(file)
        for r in t_csv:
            t_dict.append(r)
    return t_dict


def f_write(t_dict):
    with open("my_json.json", "w", encoding="utf-8") as file2:
        file2.write(json.dumps(t_dict, indent=4))


if __name__ == "__main__":

    slownik = []

    slownik = f_read(slownik)

    print(slownik)

    for i in slownik:
        try:
            j = int(i["Ilosc"])
            j += 10
            i["Ilosc"] = str(j)
        except ValueError:
            print(f"W polu ILOŚĆ dla pozycji {i} znajduje sie wartosc nieliczbowa!")


    f_write(slownik)
