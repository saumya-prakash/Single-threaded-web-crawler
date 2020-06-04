from Extra import *

import mysql.connector as sqltor

mycon = sqltor.connect(user='saumya', passwd='2020', host='localhost', database='project')

curs = mycon.cursor()

query = '''select name, home_page from records;'''

curs.execute(query)

for i in curs.fetchall():

    soup = BeautifulSoup(load_page(i[1]), features='lxml', parse_only=SoupStrainer('base'))

    a = soup.find_all('base')
    if len(a)>0:
        print(i[0])
    for tag in a:
        print(tag)


curs.close()
mycon.close()