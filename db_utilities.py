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
              "design": "designing", "(fashion)|(nift)|(n.i.f.t)|(n\.i\.f\.t)": "fashion", "animat":"animation", "graphic":"graphics",
              "professio":"professional",
              "journali":"journalism",
              "law":"law",
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


def set_type():
    try:
        mycon = connect()

    except Exception as e:
        print("Error connecting to database ->", e)

    else:

        curs = mycon.cursor()
        curs.execute("SELECT id, name FROM records WHERE type IS NULL")

        for row in curs.fetchall():
            name = row[1]  # name of the institution
            res = institution_type(name)

            if res != '':
                query = "UPDATE records SET type = \"" + res + "\" WHERE id = " + str(row[0])
                curs.execute(query)
                mycon.commit()
                print(query)

        curs.close()
        mycon.close()


def home_page_normalizer():
    try:
        mycon = connect()

    except Exception as e:
        print("Error connecting to database")

    else:
        curs = mycon.cursor()

        query = "SELECT id, home_page FROM records";
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

                try:
                    query = "UPDATE records SET home_page = " + "\'" + new_link + "\'" + " WHERE id = " + str(id) ;
                    print(query)
                    curs.execute(query)
                    mycon.commit()
                except Exception as e:
                    print(id, link)
                    print(e)
                    print()


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
        query = ''' SELECT id FROM records  '''
        curs.execute(query)

        data = curs.fetchall()

        for row in data:
            id = row[0]
            res = 'y'    # keeping default as 'y'

            store = "/home/saumya/Desktop/DATA/"

            if os.path.isfile(store+str(id)) == False:
                res = 'n'

            query = " UPDATE records SET logo_found = \'" + res + "\' " + "WHERE id = " + str(id)
            curs.execute(query)
            mycon.commit()
            # print(query)

        curs.close()
        mycon.close()

    # reverse check also required -> id not in the database but associated logo file still present -> delete such file
    files = os.listdir(store)
    for a in files:
        flag = 0
        for row in data:
            if a == str(row[0]):
                flag = 1
                break

        if flag == 0:     # id not in database
            os.remove(store+a)
            print(a, "deleted")


def table_transfer():
    try:
        mycon = connect()

    except Exception as e:
        print(e)

    else:
        curs = mycon.cursor()

        query = "SELECT name, home FROM temp"
        curs.execute(query)

        data = curs.fetchall()

        for row in data:
            name = row[0]
            home = row[1]

            query = "INSERT INTO records(name, home_page) VALUES ('%s', '%s')" % (name, home)
            try:
                curs.execute(query)
                mycon.commit()
            except Exception as e:
                print(e)
                print(query)
                print()

        curs.close()
        mycon.close()



if __name__ == '__main__':
    # home_page_normalizer()
    # protocol_resolver()
    # logo_field_checker()
    table_transfer()
    set_type()
    print()