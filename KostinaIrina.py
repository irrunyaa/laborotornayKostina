import csv
with open('FIOandTelephone.csv', 'r',encoding = "utf-8-sig") as r:
    text = csv.DictReader(r)
    a = input("Введите ФИО: ")
    for row in text:
        if a == row['FIO']:
            print(row['Telephone'])
        else:
            continue
