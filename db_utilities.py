from modules import *
import mysql.connector as sqltor
from url_utilities import load_page


def connect():
    return sqltor.connect(host='localhost', user='saumya', passwd='2020', database='project')

def institution_type(name):
    fields = {"school": "school", "engineer": "engineering", "technolog": "technology", "medical": "medical",
              "college": "college", "research": "research", "scien": "science", "universit": "university",
              "arts": "arts", "manag": "management", "social": "social", "humanit": "humanities",
              "train": "training", "(comput)|(program(m)?)|(cod)": "computer", "design": "designing",
              "fashion": "fashion", "polytechni": "polytechnic"}

    res = ''     # result to be returned

    for i in fields:
        if bool(re.search(i, name, re.IGNORECASE)):
            res += fields[i] + ' '

    return res[:-1]


def home_page_normalizer():
    try:
        mycon = sqltor.connect(host='localhost', user='saumya', passwd='2020', database='project')

    except Exception as e:
        print("Error connecting to database")

    else:
        curs = mycon.cursor()

        query = '''    SELECT id, home_page from records     ''';

        curs.execute(query)

        for row in curs.fetchall():
            id = row[0]
            link = row[1]

            try:
                ht = load_page(link)

            except Exception as e:
                print(id, link)
                print(e)
                print()

            else:
                new_link = ht.geturl()

                if link == new_link:
                    continue

                query = " UPDATE records SET home_page = " + "\'" + new_link + "\'" + " WHERE id = " + str(id) ;
                print(query)
                curs.execute(query)
                mycon.commit()


        curs.close()
        mycon.close()

if __name__ == '__main__':
    home_page_normalizer()
