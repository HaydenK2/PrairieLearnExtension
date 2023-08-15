import json

event_data = []
f = open('JSON\sample.json')

data = json.load(f)
for i in data:
    print(i["assignemntname"])
    event_data.append(i["assignemntname"])

f.close()