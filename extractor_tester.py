from Data import *
from db_utilities import *

     # required delay of websites may be stored in database -> some may not support 0 delay

try:
    mycon = connect()

except Exception as e:
    print(e)

else:
    curs = mycon.cursor()

    query = " SELECT id, home_page FROM records"
    curs.execute(query)

    a = curs.fetchall()
    curs.close()
    mycon.close()

    fi = open("LOG", "w")
    sys.stderr = fi

    stats = []
    for row in a:
        id = row[0]
        link = row[1]
        print(id, link)
        print(id, link, file=fi)

        try:
            web = Data(link)
            web.crawl(0, 30)
            s, p = get_filters()

            web.get_tsites(s, p)

            print()
            for i in web.tsites:
                print(web.scheme_dom + i)
            print()

            tmp = []    # will be appended to stats
            tmp.append(id)
            tmp.append(web.counter)
            if web.index == len(web.urls):
                tmp.append('y')
            else:
                tmp.append('n')

            tmp2 = []      # 'sites' will be stored in this

            for li in web.tsites:
                if web.check_for_download(li) == False:
                    tmp2.append(web.scheme_dom+li)

            tmp.append(tmp2)
            stats.append(tmp)

        except Exception as e:
            print("**** From TESTER ->", e, file=sys.stderr)
            print(file=sys.stderr)

    print(stats)

    mycon = connect()
    curs = mycon.cursor()

    for row in stats:
        id = row[0]
        cnt = row[1]
        comple = row[2]

        query = "UPDATE records SET examined_pages = " + str(cnt) + " , complete_crawl = \'" + comple + "\'  WHERE id = " + str(id)
        print(query)
        curs.execute(query)
        mycon.commit()

        links = row[3]     # for storing in the 'sites' table

        for li in links:
            query = "INSERT INTO sites (id, link) VALUES (" + str(id) + ", \'" + li + "\' )"
            print(query)
            try:
                curs.execute(query)
                mycon.commit()

            except Exception as e:
                print(query)
                print(e, file=sys.stderr)

    curs.close()
    mycon.close()

