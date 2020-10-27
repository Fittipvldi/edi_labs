import json, csv

with open('./json/shopping.json') as file:
    data = json.load(file)

f_csv = './gerados/shopping_answer.csv'


def total(data):
    total = 0

    for i in data['order']:
        quantity = i['quantity']
        value = i['value']
        total += value * quantity
    return total


with open(f_csv, 'w', newline='') as file:
    csv_file = csv.writer(file, delimiter=(','))
    csv_file.writerow(['ID', 'name', 'description', 'quantity', 'value', 'total'])
    for i in data['order']:
        csv_file.writerow([i['id'], i['name'], i['description'], i['quantity'], i['value'], (i['quantity'] * i['value'])])
    csv_file.writerow(['Total', '    ', '    ', '    ', '    ', total(data)])
