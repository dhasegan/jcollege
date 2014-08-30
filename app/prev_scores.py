
from app.models import *

import json
import datetime

PREV_SCORES = []

ID_TO_EID = json.load( open('app/id_to_eid.json') )

def get_highscores_people(students):
    sorted_students = sorted(students, key=lambda x: x['points'], reverse=True)
    students_list = []
    for st in sorted_students:
        jid = st['jid']
        if st['jid'] in ID_TO_EID:
            jid = ID_TO_EID[st['jid']]
        stds = Student.objects.filter(jid=jid)
        if len(stds) == 0:
            students_list.append({
                'student': {
                    'fname': st['name'] + " '14",
                    'photourl': 'http://s3-eu-west-1.amazonaws.com/whoisjack/users/' + str(jid) + '.jpg',
                },
                'points': st['points']
            })
            continue
        elif len(stds) != 1:
            continue
        std = stds[0]
        students_list.append({
            'student': std,
            'points': st['points']
        })
    return students_list[0:100]

def get_highscores_colleges(colleges):
    sorted_colleges = sorted(colleges, key=lambda x: x['points'], reverse=True)
    colleges_list = []
    for col in sorted_colleges:
        colleges_list.append({
            'name': dict(COLLEGES)[ col['name'] ],
            'points': col['points']
        })
    return colleges_list

# Load session1 into PREV_SCORES
session1_datapoints_people = json.loads('{"time": 1393514093, "all_points": [{"points": 5, "jid": "286", "name": "Anja Djokic"}, {"points": 136, "jid": "343", "name": "Andrei Iosif Smid"}, {"points": 168, "jid": "162", "name": "Henok Girma Nida"}, {"points": 3443, "jid": "159", "name": "Siddharth Shukla"}, {"points": 326, "jid": "71", "name": "Kamila Radikovna Mustafina"}, {"points": 8, "jid": "85", "name": "Ximena Jos\\u00e9 Guevara"}, {"points": 51, "jid": "41", "name": "Enxhell M Luzhnica"}, {"points": 52, "jid": "93", "name": "Dilantha Arjuna Suriyaarachchi Perera"}, {"points": 324, "jid": "255", "name": "Chanindu Ranatunga"}, {"points": 735, "jid": "29", "name": "Uneeb Adeel Agha"}, {"points": 19, "jid": "142", "name": "Cristian Pana"}, {"points": 94, "jid": "65", "name": "Hanna Kuznetsova"}, {"points": 52, "jid": "602", "name": "Deya Kuhnle"}, {"points": 318, "jid": "398", "name": "Maria Alexandra Ilie"}, {"points": 92, "jid": "537", "name": "Timo L\\u00fccke"}, {"points": 18, "jid": "1235", "name": "Seung Gyu Im"}, {"points": 12346, "jid": "883", "name": "Sevda Pinar Kiratli"}, {"points": 4, "jid": "804", "name": "Dalia M Hashweh"}, {"points": 103, "jid": "958", "name": "Fatma Salma Houerbi"}, {"points": 615, "jid": "1033", "name": "Bharath Rabindranath Bharadwaj"}, {"points": 37, "jid": "417", "name": "Gesa Marie K\\u00f6rte"}, {"points": 120, "jid": "1063", "name": "Asfandyar Ashraf Malik"}, {"points": 2042, "jid": "1243", "name": "Alper Yildirim"}, {"points": 22, "jid": "741", "name": "Ashley Elizabeth Zheng"}, {"points": 11, "jid": "1685", "name": "Sidharth Dandekar"}, {"points": 1252, "jid": "1757", "name": "Lucie Anna Christa Maria Knor"}, {"points": 299, "jid": "1640", "name": "Oleksandra O Boychenko"}, {"points": 1163, "jid": "1567", "name": "Carmela Acevedo"}, {"points": 48, "jid": "1532", "name": "Dana M Breseman"}, {"points": 14, "jid": "1412", "name": "Michael Andargachew Mekonnen"}, {"points": 640, "jid": "1955", "name": "Cornel Maximilian Amler"}, {"points": 525, "jid": "1556", "name": "Ngoc Linh Nguyen"}, {"points": 168, "jid": "1882", "name": "Ingo Alan Wagner"}, {"points": 112, "jid": "1756", "name": "Manish Kumar"}, {"points": 3, "jid": "2532", "name": "Ali Nawaz"}, {"points": 374, "jid": "2091", "name": "Catalin Florian Perticas"}, {"points": 8, "jid": "2336", "name": "Andrei Iulian Militaru"}, {"points": 106, "jid": "2582", "name": "Francisco Diaz"}, {"points": 147, "jid": "2184", "name": "Andrei Cristian Ignat"}, {"points": 118, "jid": "2378", "name": "Dorin Gabriel Clisu"}, {"points": 44, "jid": "542", "name": "Bishesh Tiwaree"}, {"points": 175, "jid": "174", "name": "Ahmed Farooq Cheema"}, {"points": 857, "jid": "198", "name": "Tomas Pllaha"}, {"points": 94, "jid": "696", "name": "Roxana Nadrag"}, {"points": 154, "jid": "918", "name": "Gautam Rai"}, {"points": 806, "jid": "1214", "name": "Sourabh Lal"}, {"points": 18, "jid": "1110", "name": "Utz Heinrich Ermel"}, {"points": 46, "jid": "1001", "name": "Ionut Codrin Amariei"}, {"points": 58, "jid": "1725", "name": "Fiona Harnischfeger"}, {"points": 169, "jid": "1677", "name": "Emily Eva-Maria Waller"}, {"points": 99, "jid": "1570", "name": "Rubens Gomes Neto"}, {"points": 1219, "jid": "1400", "name": "Ana-Maria Brecan"}, {"points": 1, "jid": "1322", "name": "Ana Ivan"}, {"points": 1674, "jid": "1765", "name": "Nina Kr\\u00fcger"}, {"points": 70, "jid": "1623", "name": "Stiv Klaud Sherko"}, {"points": 783, "jid": "45", "name": "Albena Milkova Bogoeva"}, {"points": 61, "jid": "2339", "name": "Mihai Fieraru"}, {"points": 809, "jid": "2330", "name": "Cristian Mihai Munteanu"}, {"points": 8, "jid": "51", "name": "Maryana Yurievna Morina"}, {"points": 327, "jid": "88", "name": "Romina Nikolova Nikolova"}, {"points": 44, "jid": "184", "name": "Manish Jung Thapa"}, {"points": 3, "jid": "158", "name": "Andreea Ioana Popa"}, {"points": 318, "jid": "404", "name": "Jan-David Franke"}, {"points": 11, "jid": "187", "name": "Viktorija Paneva"}, {"points": 664, "jid": "193", "name": "Bappa Maitra"}, {"points": 38, "jid": "327", "name": "Jonathan Georg Bechtold"}, {"points": 573, "jid": "154", "name": "Razvan Ioan Panea"}, {"points": 26, "jid": "442", "name": "Louis Antoine Lagoutte"}, {"points": 124, "jid": "295", "name": "Mihai Baltac"}, {"points": 62, "jid": "344", "name": "Saad Saeed"}, {"points": 112, "jid": "334", "name": "Salman Saeed"}, {"points": 629, "jid": "857", "name": "Utkrist Adhikari"}, {"points": 1737, "jid": "974", "name": "Magda Chichifoi"}, {"points": 61, "jid": "644", "name": "Keno Tetzlaff"}, {"points": 115, "jid": "894", "name": "Alexandra Crai"}, {"points": 168, "jid": "1016", "name": "Sardar Imran Hussain Bali"}, {"points": 1155, "jid": "1260", "name": "Eric Francis Bezzam"}, {"points": 1244, "jid": "1331", "name": "Hasan Abdur Rahman"}, {"points": 202, "jid": "1548", "name": "Stephanie Catherin Castan"}, {"points": 78, "jid": "2005", "name": "Radu Bors"}, {"points": 3, "jid": "1746", "name": "Archishman Sarkar"}, {"points": 2222, "jid": "2174", "name": "Alexandru Dominic Git"}, {"points": 3287, "jid": "1836", "name": "Ricarda Marie Sch\\u00e4fer"}, {"points": 93, "jid": "1708", "name": "Joshua David Frenster"}, {"points": 168, "jid": "1643", "name": "Sarah Camargo Tomaz Cleto"}, {"points": 19, "jid": "2036", "name": "Stefan Timiras"}, {"points": 45, "jid": "1909", "name": "Tim Sudmeier"}, {"points": 101, "jid": "1672", "name": "Muhammad Hassaan Farooq"}, {"points": 4, "jid": "2392", "name": "Aleksandar Gyorev"}, {"points": 168, "jid": "2328", "name": "Tudor Olariu"}, {"points": 217, "jid": "2416", "name": "Georgi Yuliyanov Gyurchev"}, {"points": 52, "jid": "2370", "name": "Denis Rochau"}, {"points": 620, "jid": "86", "name": "Vlad Popa-Florea"}, {"points": 101, "jid": "666", "name": "Stefan Appelhoff"}, {"points": 145, "jid": "473", "name": "Lorna Helene Natalia Sch\\u00fctte"}, {"points": 198, "jid": "155", "name": "Alexandru Popa"}, {"points": 77, "jid": "763", "name": "Austin Nicholas Hugenberg"}, {"points": 400, "jid": "983", "name": "Filip Stankovski"}, {"points": 173, "jid": "943", "name": "Paola Iljazi"}, {"points": 65, "jid": "1122", "name": "Sparsh Agarwal"}, {"points": 171, "jid": "1031", "name": "Rrita Limaj"}, {"points": 5, "jid": "1553", "name": "Dmitrii Cucleschin"}, {"points": 43, "jid": "2161", "name": "Domingo Antonio Vivas Peleteiro"}, {"points": 409, "jid": "1911", "name": "Namratha Nair"}, {"points": 10, "jid": "1903", "name": "Pranta Shatabdi Majumder"}, {"points": 49, "jid": "2280", "name": "Vlad Victor Ungureanu"}, {"points": 20, "jid": "414", "name": "Nicholas Matthew Lee"}, {"points": 622, "jid": "2481", "name": "Joshan Chaudhary"}, {"points": 18, "jid": "1695", "name": "Hauke Zie\\u00c3\\u0178ler"}, {"points": 93, "jid": "1002", "name": "Aman Bhattarai"}, {"points": 16, "jid": "46", "name": "Andreea Teodora Buteata"}, {"points": 70, "jid": "2199", "name": "Suryansh Pant"}, {"points": 630, "jid": "2341", "name": "Anastasia Resteu"}, {"points": 28, "jid": "1793", "name": "Johannes Gabriel Bachhuber"}, {"points": 194, "jid": "1935", "name": "Lebriz Kiziler"}, {"points": 168, "jid": "2431", "name": "Nikolche Kolev"}, {"points": 1234, "jid": "84", "name": "Nikhil Ratna Shakya"}, {"points": 298, "jid": "1972", "name": "Fran\\u00e7oise Emiel De Sutter"}, {"points": 12345, "jid": "1188", "name": "Prabal Poudel"}, {"points": 116, "jid": "646", "name": "Miriam Isabell Wulf"}, {"points": 94, "jid": "2050", "name": "Deyan Ivelinov Ginev"}, {"points": 2777, "jid": "1399", "name": "Daniel Hasegan"}, {"points": 55, "jid": "247", "name": "Ratna Bahadur Bista"}, {"points": 144, "jid": "11189", "name": "Corneliu Claudiu Prodescu"}, {"points": 359, "jid": "2268", "name": "Cristiana Dimulescu"}, {"points": 43, "jid": "712", "name": "Mengyuan Zhang"}, {"points": 2222, "jid": "113", "name": "Risav Karna"}, {"points": 494, "jid": "1157", "name": "Dominik Kundel"}, {"points": 1239, "jid": "901", "name": "Megi Mustafai"}]}')
session1_datapoints_colleges = json.loads('[{"points": 6635, "name": "N"}, {"points": 18610, "name": "C"}, {"points": 17663, "name": "K"}, {"points": 30170, "name": "M"}]')
session1_details = {
    'name': 'February Contest',
    'time_start': datetime.datetime(year=2014, month=2, day=2),
    'time_end': datetime.datetime(year=2014, month=2, day=26),
    'students': get_highscores_people(session1_datapoints_people['all_points']),
    'colleges': get_highscores_colleges(session1_datapoints_colleges)
}
PREV_SCORES.append(session1_details)

# Load session2 into PREV_SCORES
session2_datapoints_people = json.loads('{"time": 1393801399, "all_points": [{"jid": "1708", "points": 9, "name": "Joshua David Frenster"}, {"jid": "1720", "points": 109, "name": "Jessica Geiger"}, {"jid": "1604", "points": 1, "name": "Maria Paz Pati\\u00f1o"}, {"jid": "1836", "points": 8, "name": "Ricarda Marie Sch\\u00e4fer"}, {"jid": "1731", "points": 9, "name": "Gabriela Patricia Wiederkehr"}, {"jid": "2036", "points": 8, "name": "Stefan Timiras"}, {"jid": "2332", "points": 5, "name": "George Merticariu"}, {"jid": "2174", "points": 117, "name": "Alexandru Dominic Git"}, {"jid": "2083", "points": 3, "name": "Emily Melisa Ullrich Gavilanes"}, {"jid": "2328", "points": 15, "name": "Tudor Olariu"}, {"jid": "2515", "points": 13, "name": "Martha McMillan Blackley"}, {"jid": "86", "points": 55, "name": "Vlad Popa-Florea"}, {"jid": "2565", "points": 7, "name": "Jeremy Byron Schulz"}, {"jid": "2431", "points": 3, "name": "Nikolche Kolev"}, {"jid": "2490", "points": 181, "name": "Alannah Paulina Prondzinsky"}, {"jid": "2416", "points": 9, "name": "Georgi Yuliyanov Gyurchev"}, {"jid": "103", "points": 3, "name": "Dinesh Acharya"}, {"jid": "2392", "points": 5, "name": "Aleksandar Gyorev"}, {"jid": "155", "points": 10, "name": "Alexandru Popa"}, {"jid": "628", "points": 32, "name": "Natia Murusidze"}, {"jid": "799", "points": 15, "name": "Alina N\\u00f6th"}, {"jid": "474", "points": 111, "name": "Maximilian Franz Heinze"}, {"jid": "427", "points": 3181, "name": "Nana Gurgenidze"}, {"jid": "888", "points": 59, "name": "Sopio Cheishvili"}, {"jid": "983", "points": 11, "name": "Filip Stankovski"}, {"jid": "875", "points": 526, "name": "Glendi E Maliqati"}, {"jid": "981", "points": 11, "name": "Cristina Cozari"}, {"jid": "1036", "points": 417, "name": "Sara Todorovikj"}, {"jid": "1200", "points": 152, "name": "Tim Felix Uellendahl"}, {"jid": "1188", "points": 3, "name": "Prabal Poudel"}, {"jid": "1374", "points": 55, "name": "Nina Irmgard Elisabeth Martin"}, {"jid": "1911", "points": 31, "name": "Namratha Nair"}, {"jid": "1803", "points": 57, "name": "Jean-Paul Bernhard Riffald Souza Breuer"}, {"jid": "2189", "points": 89, "name": "Daniel Jonathan Michael Lindenblatt"}, {"jid": "2030", "points": 32, "name": "Hannah Pauline Gies"}, {"jid": "2280", "points": 1, "name": "Vlad Victor Ungureanu"}, {"jid": "1307", "points": 2, "name": "Turrab Haider Awan"}, {"jid": "46", "points": 2, "name": "Andreea Teodora Buteata"}, {"jid": "1853", "points": 8, "name": "D\\u00e9sir\\u00e9e Schwindenhammer"}, {"jid": "1974", "points": 40, "name": "Christopher Michael Casebeer"}, {"jid": "2391", "points": 86, "name": "Kiril Hristov Kafadarov"}, {"jid": "1972", "points": 137, "name": "Fran\\u00e7oise Emiel De Sutter"}, {"jid": "1019", "points": 4046, "name": "Irakli Grdzelishvili"}, {"jid": "1640", "points": 3450, "name": "Oleksandra O Boychenko"}, {"jid": "850", "points": 261, "name": "Pauline Andrea Bl\\u00f6th"}, {"jid": "343", "points": 1, "name": "Andrei Iosif Smid"}, {"jid": "65", "points": 56, "name": "Hanna Kuznetsova"}, {"jid": "68", "points": 105, "name": "Jana Meixnerova"}, {"jid": "348", "points": 47, "name": "Halleluya Gashaw Yayehyirad"}, {"jid": "85", "points": 124, "name": "Ximena Jos\\u00e9 Guevara"}, {"jid": "227", "points": 33, "name": "Krishna Raj Devkota"}, {"jid": "159", "points": 55, "name": "Siddharth Shukla"}, {"jid": "162", "points": 4, "name": "Henok Girma Nida"}, {"jid": "326", "points": 35, "name": "Calum Bolland"}, {"jid": "297", "points": 14, "name": "Luka Sapundzic"}, {"jid": "41", "points": 23, "name": "Enxhell M Luzhnica"}, {"jid": "257", "points": 575, "name": "Anastasija Pejkovska"}, {"jid": "29", "points": 441, "name": "Uneeb Adeel Agha"}, {"jid": "71", "points": 25, "name": "Kamila Radikovna Mustafina"}, {"jid": "126", "points": 330, "name": "Yonathan Negussie Mengesha"}, {"jid": "915", "points": 59, "name": "Amos Rweyemamu Mushumbusi"}, {"jid": "1033", "points": 1, "name": "Bharath Rabindranath Bharadwaj"}, {"jid": "537", "points": 2, "name": "Timo L\\u00fccke"}, {"jid": "547", "points": 8, "name": "Kedest Asnake Tadesse"}, {"jid": "1063", "points": 17, "name": "Asfandyar Ashraf Malik"}, {"jid": "832", "points": 4, "name": "Maame Afua Yeboah Appiah-Nuamah"}, {"jid": "398", "points": 189, "name": "Maria Alexandra Ilie"}, {"jid": "602", "points": 3, "name": "Deya Kuhnle"}, {"jid": "417", "points": 106, "name": "Gesa Marie K\\u00f6rte"}, {"jid": "1627", "points": 2, "name": "Andrea Bernarda Pati\\u00f1o"}, {"jid": "1757", "points": 66, "name": "Lucie Anna Christa Maria Knor"}, {"jid": "1563", "points": 25, "name": "Alena di Primio"}, {"jid": "1882", "points": 57, "name": "Ingo Alan Wagner"}, {"jid": "1399", "points": 2558, "name": "Daniel Hasegan"}, {"jid": "1756", "points": 6, "name": "Manish Kumar"}, {"jid": "1935", "points": 180, "name": "Lebriz Kiziler"}, {"jid": "1556", "points": 9, "name": "Ngoc Linh Nguyen"}, {"jid": "1783", "points": 5, "name": "Vivian Emily Anna Sadler"}, {"jid": "1567", "points": 3, "name": "Carmela Acevedo"}, {"jid": "2473", "points": 3, "name": "Lava Honar Fadhil"}, {"jid": "1997", "points": 63, "name": "Maxi Paulina Bretthauer"}, {"jid": "2485", "points": 331, "name": "Ciara Ann Mulvaney"}, {"jid": "2378", "points": 4, "name": "Dorin Gabriel Clisu"}, {"jid": "2481", "points": 115, "name": "Joshan Chaudhary"}, {"jid": "1955", "points": 31, "name": "Cornel Maximilian Amler"}, {"jid": "2479", "points": 139, "name": "Hannah Fay Cherny"}, {"jid": "2582", "points": 6, "name": "Francisco Diaz"}, {"jid": "2", "points": 180, "name": "Alina Dima"}, {"jid": "2383", "points": 5, "name": "Mihai-Razvan Burai-Patrascu"}, {"jid": "153", "points": 525, "name": "Claudia Elena Loica"}, {"jid": "542", "points": 67, "name": "Bishesh Tiwaree"}, {"jid": "1003", "points": 8, "name": "Otar Bichiashvili"}, {"jid": "986", "points": 15, "name": "Syed Akber Imam Jafri"}, {"jid": "712", "points": 15, "name": "Mengyuan Zhang"}, {"jid": "1303", "points": 15, "name": "Radu Hambasan"}, {"jid": "1214", "points": 123, "name": "Sourabh Lal"}, {"jid": "1255", "points": 8, "name": "Dan Daniel Erdmann-Pham"}, {"jid": "1647", "points": 60, "name": "Victoria von Glasenapp"}, {"jid": "1583", "points": 20, "name": "Egi Bendo"}, {"jid": "1570", "points": 2, "name": "Rubens Gomes Neto"}, {"jid": "1521", "points": 11, "name": "Radu Anton"}, {"jid": "1658", "points": 11, "name": "Rebekka Schliep"}, {"jid": "1350", "points": 5, "name": "Siegfried Hoang Nguyen Wegmann"}, {"jid": "2339", "points": 15, "name": "Mihai Fieraru"}, {"jid": "2399", "points": 2, "name": "Tony Tolev Georgiev"}, {"jid": "2045", "points": 15, "name": "Lydia Elisabeth Canals"}, {"jid": "184", "points": 21, "name": "Manish Jung Thapa"}, {"jid": "91", "points": 14, "name": "Petya Georgieva Shishiteva"}, {"jid": "114", "points": 4, "name": "Remun Koirala"}, {"jid": "84", "points": 3, "name": "Nikhil Ratna Shakya"}, {"jid": "160", "points": 64, "name": "Cvetanka Jovanovska"}, {"jid": "45", "points": 101, "name": "Albena Milkova Bogoeva"}, {"jid": "154", "points": 3, "name": "Razvan Ioan Panea"}, {"jid": "304", "points": 5, "name": "Muhammad Omer Saeed"}, {"jid": "349", "points": 1, "name": "Ahmad Saeed"}, {"jid": "415", "points": 159, "name": "Agne Baltrisiunaite"}, {"jid": "974", "points": 3, "name": "Magda Chichifoi"}, {"jid": "877", "points": 6, "name": "Nyasha Godknows Majoni"}, {"jid": "901", "points": 8, "name": "Megi Mustafai"}, {"jid": "1002", "points": 22, "name": "Aman Bhattarai"}, {"jid": "1157", "points": 4, "name": "Dominik Kundel"}, {"jid": "1016", "points": 1, "name": "Sardar Imran Hussain Bali"}, {"jid": "1127", "points": 36, "name": "Naomi Pentrel"}]}')
session2_datapoints_colleges = json.loads('[{"points": 1097, "name": "N"}, {"points": 9462, "name": "M"}, {"points": 9158, "name": "K"}, {"points": 1082, "name": "C"}]')
session2_details = {
    'name': 'Arts Olympics Special Contest',
    'time_start': datetime.datetime(year=2014, month=2, day=27, hour=22),
    'time_end': datetime.datetime(year=2014, month=3, day=2, hour=23, minute=59, second=59),
    'students': get_highscores_people(session2_datapoints_people['all_points']),
    'colleges': get_highscores_colleges(session2_datapoints_colleges)
}
PREV_SCORES.append(session2_details)

# Load session3 into PREV_SCORES
session3_datapoints_people = json.loads('{"time": 1408711079, "all_points": [{"points": 1890, "name": "Kareem Al Nahas", "jid": "2009"}, {"points": 721, "name": "Bharath Rabindranath Bharadwaj", "jid": "1033"}, {"points": 6, "name": "Hasan Abdur Rahman", "jid": "1331"}, {"points": 54, "name": "Cosmin Ionut Marin", "jid": "1370"}, {"points": 19, "name": "Ricarda Marie Sch\\u00e4fer", "jid": "1836"}, {"points": 24, "name": "Hauke Zie\\u00c3\\u0178ler", "jid": "1695"}, {"points": 1, "name": "Johannes Gabriel Bachhuber", "jid": "1793"}, {"points": 121, "name": "Cristiana Dimulescu", "jid": "2268"}, {"points": 18, "name": "Albena Milkova Bogoeva", "jid": "45"}, {"points": 202, "name": "Tudor Olariu", "jid": "2328"}, {"points": 18, "name": "Emily Melisa Ullrich Gavilanes", "jid": "2083"}, {"points": 9, "name": "Radu Bors", "jid": "2005"}, {"points": 7, "name": "George Merticariu", "jid": "2332"}, {"points": 20, "name": "Stefan Timiras", "jid": "2036"}, {"points": 280, "name": "Emanuel Stiuler", "jid": "1845"}, {"points": 304, "name": "Alannah Paulina Prondzinsky", "jid": "2490"}, {"points": 243, "name": "Nikolche Kolev", "jid": "2431"}, {"points": 2222, "name": "Despina Stefanoska", "jid": "101"}, {"points": 3003, "name": "Siddharth Shukla", "jid": "159"}, {"points": 27, "name": "Aleksandar Gyorev", "jid": "2392"}, {"points": 1472, "name": "Ivona Kafedjiska", "jid": "168"}, {"points": 2, "name": "Georgi Yuliyanov Gyurchev", "jid": "2416"}, {"points": 120, "name": "Alexandru Popa", "jid": "155"}, {"points": 124, "name": "Daniela Fernandez", "jid": "2562"}, {"points": 9, "name": "Martha McMillan Blackley", "jid": "2515"}, {"points": 2, "name": "Dinesh Acharya", "jid": "103"}, {"points": 308, "name": "Elanah Lohse", "jid": "406"}, {"points": 7, "name": "Mina Khairy Nesseim Khalil Salib", "jid": "272"}, {"points": 35, "name": "Austin Nicholas Hugenberg", "jid": "763"}, {"points": 9, "name": "Alina N\\u00f6th", "jid": "799"}, {"points": 59, "name": "Stefan Appelhoff", "jid": "666"}, {"points": 8, "name": "Maximilian Franz Heinze", "jid": "474"}, {"points": 545, "name": "Franziska Neumann", "jid": "1381"}, {"points": 120, "name": "Prabal Poudel", "jid": "1188"}, {"points": 3, "name": "Sopio Cheishvili", "jid": "888"}, {"points": 6, "name": "Jinqian Li", "jid": "1020"}, {"points": 137, "name": "Sparsh Agarwal", "jid": "1122"}, {"points": 408, "name": "Rrita Limaj", "jid": "1031"}, {"points": 48, "name": "Filip Stankovski", "jid": "983"}, {"points": 454, "name": "Sara Todorovikj", "jid": "1036"}, {"points": 11, "name": "Namratha Nair", "jid": "1911"}, {"points": 27, "name": "Alan \\u00d6zalp", "jid": "1663"}, {"points": 8, "name": "Jean-Paul Bernhard Riffald Souza Breuer", "jid": "1803"}, {"points": 7, "name": "Daniel Jonathan Michael Lindenblatt", "jid": "2189"}, {"points": 9, "name": "Vlad Victor Ungureanu", "jid": "2280"}, {"points": 8, "name": "Hannah Pauline Gies", "jid": "2030"}, {"points": 1, "name": "Denis Rochau", "jid": "2370"}, {"points": 35, "name": "Andrei George Giurgiu", "jid": "2315"}, {"points": 281, "name": "Anastasia Resteu", "jid": "2341"}, {"points": 7, "name": "Kiril Hristov Kafadarov", "jid": "2391"}, {"points": 27, "name": "Christopher Michael Casebeer", "jid": "1974"}, {"points": 200, "name": "Fran\\u00e7oise Emiel De Sutter", "jid": "1972"}, {"points": 20, "name": "Johannes Niklas Hansen", "jid": "1369"}, {"points": 17, "name": "Calum Bolland", "jid": "326"}, {"points": 3337, "name": "Oleksandra O Boychenko", "jid": "1640"}, {"points": 41, "name": "Andrei-Mihai Nicolae", "jid": "461"}, {"points": 507, "name": "D\\u00e9sir\\u00e9e Schwindenhammer", "jid": "1853"}, {"points": 201, "name": "Pauline Andrea Bl\\u00f6th", "jid": "850"}, {"points": 211, "name": "Vasco Braz\\u00c3\\u00a3o", "jid": "1641"}, {"points": 65, "name": "Krishna Raj Devkota", "jid": "227"}, {"points": 6, "name": "Ratna Bahadur Bista", "jid": "247"}, {"points": 802, "name": "Kamila Radikovna Mustafina", "jid": "71"}, {"points": 9, "name": "Chanindu Ranatunga", "jid": "255"}, {"points": 29, "name": "Cera Alexandra McDonald", "jid": "337"}, {"points": 258, "name": "Cristian Pana", "jid": "142"}, {"points": 8, "name": "Andreea Ciuprina", "jid": "241"}, {"points": 340, "name": "Uneeb Adeel Agha", "jid": "29"}, {"points": 7, "name": "Yonathan Negussie Mengesha", "jid": "126"}, {"points": 23, "name": "Enxhell M Luzhnica", "jid": "41"}, {"points": 78, "name": "Dilantha Arjuna Suriyaarachchi Perera", "jid": "93"}, {"points": 14, "name": "Anastasija Pejkovska", "jid": "257"}, {"points": 42, "name": "Andrei Iosif Smid", "jid": "343"}, {"points": 73, "name": "Asfandyar Ashraf Malik", "jid": "1063"}, {"points": 27, "name": "Yohana Tesfamariam", "jid": "1226"}, {"points": 71, "name": "Kedest Asnake Tadesse", "jid": "547"}, {"points": 500, "name": "Gabriela Rodica Constantin-Dureci", "jid": "862"}, {"points": 121, "name": "Dalia M Hashweh", "jid": "804"}, {"points": 339, "name": "Maria Alexandra Ilie", "jid": "398"}, {"points": 135, "name": "Gesa Marie K\\u00f6rte", "jid": "417"}, {"points": 43, "name": "Sevda Pinar Kiratli", "jid": "883"}, {"points": 1, "name": "Timo L\\u00fccke", "jid": "537"}, {"points": 67, "name": "Deya Kuhnle", "jid": "602"}, {"points": 5, "name": "Seung Gyu Im", "jid": "1235"}, {"points": 214, "name": "Ingo Alan Wagner", "jid": "1882"}, {"points": 3, "name": "Manish Kumar", "jid": "1756"}, {"points": 18, "name": "Matthias Aengenheyster", "jid": "1781"}, {"points": 1, "name": "Birte Martina Nicola Schulze Raestrup", "jid": "1660"}, {"points": 79, "name": "Alina Stein", "jid": "1413"}, {"points": 625, "name": "Lebriz Kiziler", "jid": "1935"}, {"points": 3372, "name": "Daniel Hasegan", "jid": "1399"}, {"points": 151, "name": "Ngoc Linh Nguyen", "jid": "1556"}, {"points": 213, "name": "Marie Ritter", "jid": "1818"}, {"points": 2, "name": "Lucie Anna Christa Maria Knor", "jid": "1757"}, {"points": 3, "name": "Abbey Marie Taylor", "jid": "1908"}, {"points": 300, "name": "Dorin Gabriel Clisu", "jid": "2378"}, {"points": 24, "name": "Maxi Paulina Bretthauer", "jid": "1997"}, {"points": 1553, "name": "Catalin Florian Perticas", "jid": "2091"}, {"points": 34, "name": "Andrei Cristian Ignat", "jid": "2184"}, {"points": 402, "name": "Joshan Chaudhary", "jid": "2481"}, {"points": 9, "name": "Mihai-Razvan Burai-Patrascu", "jid": "2383"}, {"points": 246, "name": "Cornel Maximilian Amler", "jid": "1955"}, {"points": 20, "name": "Ahmed Farooq Cheema", "jid": "174"}, {"points": 250, "name": "Bishesh Tiwaree", "jid": "542"}, {"points": 58, "name": "Tomas Pllaha", "jid": "198"}, {"points": 641, "name": "Claudia Elena Loica", "jid": "153"}, {"points": 12, "name": "Otar Bichiashvili", "jid": "1003"}, {"points": 9, "name": "Syed Zaada Mouhammad Alee Kazmi", "jid": "881"}, {"points": 5, "name": "Jiaqi Song", "jid": "714"}, {"points": 24, "name": "Cornel Amariei", "jid": "1018"}, {"points": 1, "name": "Mengyuan Zhang", "jid": "712"}, {"points": 124, "name": "Kristi Gadeshi", "jid": "869"}, {"points": 5, "name": "Gautam Rai", "jid": "918"}, {"points": 11, "name": "Fawaz-ul Haq", "jid": "1673"}, {"points": 7, "name": "Joseph Isai Avenda\\u00f1o", "jid": "1637"}, {"points": 13, "name": "Stiv Klaud Sherko", "jid": "1623"}, {"points": 3, "name": "Marius Remus Dumitrel", "jid": "1107"}, {"points": 3, "name": "Utz Heinrich Ermel", "jid": "1110"}, {"points": 8, "name": "Rebekka Schliep", "jid": "1658"}, {"points": 1147, "name": "Sourabh Lal", "jid": "1214"}, {"points": 6, "name": "Radu Hambasan", "jid": "1303"}, {"points": 7, "name": "Dan Daniel Erdmann-Pham", "jid": "1255"}, {"points": 26, "name": "Mihai Fieraru", "jid": "2339"}, {"points": 8, "name": "Luiscarlos A Torres", "jid": "2094"}, {"points": 767, "name": "Nina Kr\\u00fcger", "jid": "1765"}, {"points": 1, "name": "Andreea Adriana Neamtu", "jid": "2306"}, {"points": 8, "name": "Razvan Barabas", "jid": "2143"}, {"points": 34, "name": "Yingzhao Zhu", "jid": "2294"}, {"points": 95, "name": "Bianca Mocanu", "jid": "2307"}, {"points": 45, "name": "Michael Kardalinos", "jid": "2053"}, {"points": 77, "name": "Muhammad Omer Saeed", "jid": "304"}, {"points": 162, "name": "Laura Maria Garcia", "jid": "63"}, {"points": 18, "name": "Anirudh Bayanwala", "jid": "176"}, {"points": 4, "name": "Manish Jung Thapa", "jid": "184"}, {"points": 26, "name": "Razvan Ioan Panea", "jid": "154"}, {"points": 14, "name": "Nikhil Ratna Shakya", "jid": "84"}, {"points": 71, "name": "Jonathan Georg Bechtold", "jid": "327"}, {"points": 26, "name": "Faryal Khalid", "jid": "347"}, {"points": 1, "name": "Julian Jannik Hohrath", "jid": "787"}, {"points": 29, "name": "Miriam Isabell Wulf", "jid": "646"}, {"points": 19, "name": "Mahlet Taddese Sahle", "jid": "529"}, {"points": 158, "name": "Louis Antoine Lagoutte", "jid": "442"}, {"points": 176, "name": "Danielle Joy Dayhoff", "jid": "653"}, {"points": 6, "name": "Magda Chichifoi", "jid": "974"}, {"points": 21, "name": "Nyasha Godknows Majoni", "jid": "877"}, {"points": 13, "name": "Aman Bhattarai", "jid": "1002"}, {"points": 4, "name": "Fatjon Meci", "jid": "940"}, {"points": 40, "name": "Tobias Schraink", "jid": "1083"}, {"points": 225, "name": "Dominik Kundel", "jid": "1157"}, {"points": 5, "name": "Sardar Imran Hussain Bali", "jid": "1016"}]}')
session3_datapoints_colleges = json.loads('[{"points": 18158, "name": "M"}, {"points": 5228, "name": "N"}, {"points": 6550, "name": "K"}, {"points": 2829, "name": "C"}]')
session3_details = {
    'name': 'Rest of Spring 2014 Contest',
    'time_start': datetime.datetime(year=2014, month=3, day=8, hour=12),
    'time_end': datetime.datetime(year=2014, month=6, day=6, hour=23, minute=59, second=59),
    'students': get_highscores_people(session3_datapoints_people['all_points']),
    'colleges': get_highscores_colleges(session3_datapoints_colleges)
}
PREV_SCORES.append(session3_details)