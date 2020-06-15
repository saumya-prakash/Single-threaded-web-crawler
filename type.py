import mysql.connector as sqltor
from db_utilities import *

try:
    mycon=sqltor.connect(host="localhost", user="saumya", passwd="2020", database="project")
except Exception as e:
    print(e)
else:

    curs=mycon.cursor()
    curs.execute("SELECT id, name FROM records WHERE type IS NULL")

    for data in curs.fetchall():
        name = data[1]   # name of the institution
        res = institution_type(name)

        if res!='':
            query="UPDATE records SET type=\""+res+"\" WHERE id="+str(data[0])
            curs.execute(query)
            mycon.commit()
            print(query)

    curs.close()
    mycon.close()