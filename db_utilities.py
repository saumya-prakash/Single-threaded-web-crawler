from modules import *
import mysql.connector as sqltor
from url_utilities import load_page


def connect():
    return sqltor.connect(host='localhost', user='saumya', passwd='2020', database='project')


def institution_type(name):
    fields = {
              "school": "school",
              "engineer": "engineering", "technolog": "technology", "polytechni": "polytechnic",
              "medical": "medical", "dent":"dental",
              "research": "research", "scien": "science",
              "college": "college", "universit": "university",
              "arts": "arts", "manag": "management", "social": "social", "humanit": "humanities",
              "train": "training", "(comput)|(program(m)?)|(cod)": "computer",
              "design": "designing", "fashion": "fashion", "animat":"animation", "graphic":"graphics",
              "professio":"professional",
              "journali":"journalism",
              "meteorolog":"meteorology",
              "beaut":"beauty",
              "langua":"language",
              # "hotel":"hotel"
               "women|girl|lad(y|i)":"women"
              }

    res = ''     # result to be returned

    for i in fields:
        if bool(re.search(i, name, re.IGNORECASE)):
            res += fields[i] + ' '

    return res[:-1]


def home_page_normalizer():
    try:
        mycon = connect()

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


def protocol_resolver():
    try:
        mycon = connect()

    except Exception as e:
        print("Error connecting to the database ->", e)

    else:
        curs = mycon.cursor()

        query = ''' SELECT id, home_page FROM records WHERE home_page NOT LIKE \'http%\'  '''

        curs.execute(query)

        for row in curs.fetchall():
            id = row[0]
            link = row[1]
            print(id)

            url = ''

            try:
                ht = load_page('https://' + link)
                url = ht.geturl()

            except Exception as e:
                print(e)
                try:
                    ht = load_page('http://' + link)
                    url = ht.geturl()

                except Exception as f:
                    print(f)

            if url == '':
                continue

            query = "  UPDATE records SET home_page = " + "\'" + url + "\' " + "WHERE id = " + str(id);
            print(query)
            print()
            curs.execute(query)

        mycon.commit()
        curs.close()
        mycon.close()


def logo_field_checker():           # checks if the entry in database in consistent with the actual data
    try:
        mycon = connect()

    except Exception as e:
        print("Error connecting to database ->", e)

    else:
        curs = mycon.cursor()
        query = ''' SELECT id, name FROM records  '''
        curs.execute(query)

        for row in curs.fetchall():
            id = row[0]
            name = row[1]
            res = 'y'    # keeping default as 'y'

            store = "/home/saumya/Desktop/DATA/"

            if os.path.isdir(store+name) == False:
                res = 'n'

            if res == 'y':
                os.chdir(store+name)
                if os.path.isfile("./aaa_logo") == False:        # aaa_logo not present
                    res = 'n'
                os.chdir("./../")


            query = " UPDATE records SET logo = \'" + res + "\' " + "WHERE id = " + str(id)
            curs.execute(query)
            mycon.commit()
            # print(query)


        curs.close()
        mycon.close()




if __name__ == '__main__':
    # home_page_normalizer()
    # protocol_resolver()
    logo_field_checker()
    print()