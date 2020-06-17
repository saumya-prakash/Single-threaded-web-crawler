import mysql.connector as sqltor
from db_utilities import *

try:
    mycon = connect()

except Exception as e:
    print("Error connecting to database ->", e)

else:

    curs=mycon.cursor()
    curs.execute("SELECT id, name FROM records WHERE type IS NULL")

    for row in curs.fetchall():
        name = row[1]   # name of the institution
        res = institution_type(name)

        if res != '':
            query = "UPDATE records SET type = \"" + res + "\" WHERE id = "+str(row[0])
            curs.execute(query)
            mycon.commit()
            print(query)

    curs.close()
    mycon.close()