
import json

idtoeid = {}
colleges = ["mercator", "krupp", "college-III", "nordmetall"]

for col in colleges:
    json_file = open(col + ".json")
    students = json.load(json_file)
    for st in students:
        idtoeid[ st['id'] ] = st['eid']

eids = open('id_to_eid.json', 'w')
eids.write( json.dumps(idtoeid) )
eids.close()