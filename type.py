import mysql.connector as sqltor
import re

try:
    mycon=sqltor.connect(host="localhost", user="saumya", passwd="2020", database="project")
except Exception as e:
    print(e)
else:

    field={".*school.*":"school", ".*engineer.*":"engineering", ".*technology.*":"technology", ".*medical.*":"medical",
           ".*college.*":"college",".*research.*":"research", ".*science.*":"science", ".*university.*":"university",
           ".*arts.*":"arts", ".*manage.*":"management", ".*social.*":"social", ".*humanity.*":"humanities",
           ".*train.*":"training", "(.*comput.*)|(.*program(me)?.*)|(.*cod.*)":"computer", ".*design.*":"designing",
           ".*fashion.*":"fashion", ".*polytechni.*":"polytechnic"}

    curs=mycon.cursor()
    curs.execute("SELECT * FROM records")

    for data in curs.fetchall():
        s=data[1]
        res=''
        for key in field:
            if bool(re.match(key, s, re.IGNORECASE)):
                res+=field[key]+" "

        if res!='':
            res=res[:len(res)-1]
            query="update records set type=\""+res+"\" where id="+str(data[0])
            curs.execute(query)
    		mycon.commit()
            print(query)

    curs.close()
    mycon.close()