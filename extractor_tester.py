from Data import *
from db_utilities import *

     # required delay of websites may be stored in database -> some may not support 0 delay

try:
    mycon = connect()

except Exception as e:
    print(e)

else:
    curs = mycon.cursor()

    query = " SELECT id, home_page FROM records  WHERE id != 28 "
    curs.execute(query)

    a = curs.fetchall()

    curs.close()
    mycon.close()

    for row in a:
        id = row[0]
        link = row[1]
        print(id, link)

        try:
            web = Data(link)
            web.crawl(0, 200)
            s, p = get_filters()

            web.get_tsites(s, p)

            print()
            for i in web.tsites:
                print(web.scheme_dom + i)
            print()

        except Exception as e:
            print("**** From TESTER ->", e)
            print()


