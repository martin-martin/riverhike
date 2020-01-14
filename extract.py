import re
import json
from bs4 import BeautifulSoup
from pprint import pprint
from jinja2 import Template


with open('index_old.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

tables = soup.find_all('table')
# print(len(tables))

data = []
for table in tables:
    #pprint(table)
    cols = table.find('thead').findChildren()
    # for c in cols:
    #     print(c.text)

    headers = [header.text for header in table.find_all("th")]
    # results = [{headers[i]: cell.text for i, cell in enumerate(row.find_all("td"))}
    #            for row in table.find_all("tr")]
    results = [[cell.text for cell in row.find_all("td")] for row in table.find_all("tr")]
    data.append((headers, results))


for table in data:
    if any([re.findall(r'image', heading.lower()) for heading in table[0]]):
        print(table[0])
        for row in table[1]:
            if row:
                row[0] = row[1].lower() + '.png'
    # print([re.findall(r'image', heading.lower()) for heading in table[0]])

raw = Template("""{% for table in data %}<table>
    <thead>
    <tr>{% for header in table[0] %}
        <th>{{ header }}</th>{% endfor %}
    </tr>
    </thead>
    <tbody>{% for row in table[1] %}
        <tr>{% for cell in row %}
            <td>{{ cell }}</td>{% endfor %}
        </tr>{% endfor %}
    </tbody>
</table>
{% endfor %}
""")

pprint(data)

html = raw.render(data=data)

with open('tables.html', 'w') as fout:
    fout.write(html)

with open('tables.json', 'w') as fout:
    json.dump(data, fout)
