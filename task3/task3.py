import json
with open("task3/tests.json", "r") as y:
    tests = json.load(y)
with open("task3/values.json", "r") as f:
    values = json.load(f)

def fill_json(json1, json2):
    for i in json1:
        for v in json2['values']:
            if i.get('id') == v.get('id'):
                i['value'] = v.get('value')
                break
        if 'values' in i.keys():
            fill_json(i['values'], json2)
    print(json1)
    with open('task3/output.json', 'w') as outfile:
        json.dump(json1, outfile)
fill_json(tests['tests'],values)

