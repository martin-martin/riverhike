import json
from pprint import pprint


with open('tables.json', 'r') as fin:
    data = json.load(fin)

adapdata = []

for table in data:
    temp = dict()
    temp['header'] = table[0]
    temp['content'] = []
    for row in table[1]:
        if row:
            r = {table[0][i].lower(): cell for i, cell in enumerate(row, start=0)}
            temp['content'].append(r)
    adapdata.append(temp)

pprint(adapdata)