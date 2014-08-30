import json

list_of_colleges = ['mercator','nordmetall','college-III','krupp']
username_to_email = {}

id_of_imgs = json.load( open("has_images.json") )

for col in list_of_colleges:
    f = open(col + ".json")
    students = json.load(f)
    for student in students:
        if "account" in student and "email" in student:
            if student['account'] not in username_to_email:
                username_to_email[student['account']] = {
                    "email": student['email'],
                    "first_name": student['fname'],
                    "last_name": student['lname'],
                    "eid": student['eid']
                }
                if "year" in student and student['year']:
                    username_to_email[student['account']]['year'] = student['year']
                if "description" in student and student['description']:
                    username_to_email[student['account']]['description'] = student['description']
                if int(student['eid']) in id_of_imgs:
                    username_to_email[student['account']]['photourl'] = "https://s3-eu-west-1.amazonaws.com/whoisjack/users/" + student['eid'] + ".jpg"
            else:
                print "Duplicate for ", student['account'], "with", student['email'], " and ", username_to_email[student['account']]


result = json.dumps(username_to_email)
user_to_email_file = open("jacobs_user_details.json", "w")
user_to_email_file.write(result)
user_to_email_file.close()