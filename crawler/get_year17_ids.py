
import json

freshman_ids = []
colleges = ["mercator", "krupp", "college-III", "nordmetall"]

for col in colleges:
    json_file = open(col + ".json")
    students = json.load(json_file)
    for st in students:
        if "year" in st and st["year"] == "17":
            freshman_ids.append( st["eid"] )
