import json, csv

f_csv = './gerados/shopping_answer.csv'
f_json = './gerados/shopping_answer.json'

with open(f_csv, 'r') as file:
    csv_file = csv.DictReader(file)
    data = {'order': []}
    for i in csv_file:
        data['order'].append(i)

with open(f_json, 'w') as file:
    file.write(json.dumps(data, indent=4))
