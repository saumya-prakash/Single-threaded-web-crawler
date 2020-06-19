from Data import *
from db_utilities import *


logo_field_checker()

mycon = connect()

curs = mycon.cursor()

query = ''' SELECT id, name, home_page from records WHERE logo = 'n'  '''

curs.execute(query)

for row in curs.fetchall():
    id = row[0]
    name = row[1]
    hp = row[2]

    store = "/home/saumya/Desktop/DATA/"

    if os.path.isdir(store+name) == False:
        os.mkdir(store+name)

    os.chdir(store+name)

    print(name)
    try:
        web = Data(hp)
        web.get_logo()

    except Exception as e:
        print(e)

    if os.path.isfile("./aaa_logo"):
        query = " UPDATE records SET logo = \'y\' WHERE ID = " + str(id)
        curs.execute(query)
        print(query)
        mycon.commit()

    print()
    os.chdir("./../")

curs.close()
mycon.close()
