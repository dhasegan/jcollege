import json

list_of_colleges = ['Mercator','Nordmetall','C3','Krupp']

json_file = open("crawler/class2017.json")
students = json.load(json_file)

pth_file = open("crawler/phone_to_room.json")
phone_to_room = json.load(pth_file)

images = []

for col in list_of_colleges:
    parsed_students = []
    for st in students:
        if not st["college"] == col:
            continue
        if st["phone"] in phone_to_room:
            st["room"] = phone_to_room[st["phone"]]
        parsed_students.append(st)
        images.append( st['photo'] )

    # print students in files
    result = json.dumps(parsed_students)
    json_file = open("crawler/"+col+".json", "w")
    json_file.write(result)
    print col, len(parsed_students)

# print images
result = json.dumps(images)
json_file = open("crawler/images_links.json", "w")
json_file.write(result)