import json, csv
from convert_json_to_csv import total

with open('./json/shopping.json') as file:
    data_json = json.load(file)

f_csv = './gerados/shopping_answer.csv'
f_json = './gerados/shopping_answer.json'

with open(f_csv, 'r') as file:
    csv_file = csv.DictReader(file)
    data = {'order': []}
    for i in csv_file:
        if(i['ID'] == 'Total'):
            pass
        else:
            data['order'].append(i)

    data['total'] = total(data_json)

with open(f_json, 'w') as file:
    file.write(json.dumps(data, indent=4))
