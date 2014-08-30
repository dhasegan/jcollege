import json
from app.models import *
from collections import OrderedDict

def get_bad_ids(filename):
    ids = [line.strip() for line in open(filename)]
    return ids

years = ["15", "16", "17"]

def college_to_database(college_name):
    json_file = open("crawler/" + college_name + ".json")
    json_data = json.load(json_file)
    for juser in json_data:
        jid = juser['eid']
        bad_ids = get_bad_ids("crawler/"+"bad_ids.txt")
        major = juser['major']
        exmat = major.find('exmatr')
        year = juser["year"]
        if exmat == -1 and not (jid in bad_ids) and year in years:
            major_list = ['CS', 'EECS', 'ECE', 'ESS', 'EE', 'ACM', 'PHY', 'BCCB', 'BCE', 'IRB', 'ISCP', 'IES', 'ICS', 'ISS', 'ILME', 'CPN', 'MATH', 'GEM', 'BIOCHEM', 'CHEM', 'BIOTECH', 'BIGSSS', 'IR', 'IMS', 'IL', 'BIO/NEURO', 'GH']
            majors = ''
            for major_name in major_list:
                found = major.find(major_name)
                if found != -1:
                    majors = majors + major_name + ' '
            if len(majors) != 0:
                majors = majors[:-1]
            password = '1234'
            photourl = juser['photo']
            photourl = photourl.replace('http://swebtst01.public.jacobs-university.de/jPeople/image.php?id=', 'http://s3-eu-west-1.amazonaws.com/whoisjack/users/') + ".jpg"
            if True:
                new_juser = Student(jid = jid,\
                    fname = juser['fname'],\
                    lname = juser['lname'],\
                    email = juser['email'],\
                    college = college_name[0].upper(),\
                    room = juser.get('room'),\
                    phone = juser['phone'],\
                    country = juser['country'],\
                    username = juser['account'],\
                    password = password,\
                    is_active = False,\
                    majorinfo = juser['majorinfo'],\
                    majorlong = juser['majorlong'],\
                    major = majors,\
                    year = juser['year'],\
                    photourl = photourl)
                new_juser.set_password(password)
                new_juser.save()


list_of_colleges = ['mercator','nordmetall','college-III','krupp']

for college in list_of_colleges:
    college_to_database(college)

College(name="M").save()
College(name="K").save()
College(name="C").save()
College(name="N").save()

MAJOR_TO_MAJOR = {
    'CS ICS': 'ICS',
    'CS EECS EE': 'EECS',
    'ILME IL': 'ILME',
    'IRB IR': 'IRB'
}

students = Student.objects.all()
for st in students:
  if st.major in MAJOR_TO_MAJOR:
    st.major = MAJOR_TO_MAJOR[ st.major ]
    st.save()

for st in students:
    if st.major in major_list:
        st.major = major_list[ st.major ]
        st.save()


# Populate answers
answers = json.load( open('crawler/answers.json') )
for answer in answers:
    students = Student.objects.filter(username=answer['username'])
    if len(students) == 1:
        st = students[0]
        sqa = SpecialQuestionAnswer.objects.create(student=st, qtype=answer['qtype'],\
            college=st.college, answer=answer['answer'])

