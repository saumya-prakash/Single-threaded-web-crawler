from Data import *
from db_utilities import *

     # required delay of websites may be stored in database -> some may not support 0 delay

try:
    mycon = connect()

except Exception as e:
    print(e)

else:
    curs = mycon.cursor()

    query = " SELECT id, home_page FROM records  WHERE id > 31 "
    curs.execute(query)

    a = curs.fetchall()

    curs.close()
    mycon.close()

    fi = open("LOG", "w")

    sys.stderr = fi

    for row in a:

        id = row[0]
        link = row[1]
        print(id, link)
        print(id, link, file=fi)

        try:
            web = Data(link)
            web.crawl(0, 20)
            s, p = get_filters()

            web.get_tsites(s, p)

            print()
            for i in web.tsites:
                print(web.scheme_dom + i)
            print()

        except Exception as e:
            print("**** From TESTER ->", e, file=sys.stderr)
            print(fiel=sys.stderr)


