from Data import *
from db_utilities import *


logo_field_checker()

mycon = connect()
curs = mycon.cursor()

query = " SELECT id, home_page FROM records WHERE logo_found = 'n'  "
curs.execute(query)

for row in curs.fetchall():
    id = row[0]
    hp = row[1]

    store = "/home/saumya/Desktop/DATA_alt/"
    os.chdir(store)

    try:
        web = Data(hp)
        image = web.get_logo()

    except Exception as e:
        print(id, hp, e)
        print()

    else:
        if image is not None:
            with open(str(id), 'wb') as fi:
                fi.write(image.read())

            query = " UPDATE records SET logo_found = \'y\' WHERE ID = " + str(id)
            curs.execute(query)
            mycon.commit()
            # print(query)


curs.close()
mycon.close()
