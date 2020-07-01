from db_utilities import *

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

        query = "INSERT INTO records(name, home_page) VALUES ('%s', '%s')" %(name, home)
        try:
            curs.execute(query)
            mycon.commit()
        except Exception as e:
            print(e)
            print(query)
            print()


    curs.close()
    mycon.close()