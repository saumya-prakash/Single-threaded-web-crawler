from Data import *
from db_utilities import *


logo_field_checker()     # to make the data in the folder and the database consistent

mycon = connect()        # connection instance to the database
curs = mycon.cursor()

query = " SELECT id, home_page FROM records WHERE logo_found = 'n' order by id desc"
curs.execute(query)

for row in curs.fetchall():
    id = row[0]
    hp = row[1]

    store = "/home/saumya/Desktop/logos/"
    os.chdir(store)

    try:
        web = Data(hp)
        u = web.get_logo()     # getting the link to the logo

    except Exception as e:
        print(id, hp, e)
        print()

    else:
        if u is not None and u != '':
            try:
                image = load_page(u)

            except Exception as e:
                print(id, hp, e)

            else:
                with open(str(id), 'wb') as fi:
                    fi.write(image.read())

                query = " UPDATE records SET logo_found = \'y\' WHERE ID = " + str(id)
                curs.execute(query)
                mycon.commit()
                # print(query)


curs.close()
mycon.close()
