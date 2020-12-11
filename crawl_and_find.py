from Data import *
from db_utilities import *

     # required delay of websites may be stored in database -> some may not support 0 delay

try:
    mycon = connect()

except Exception as e:
    print(e)

else:
    curs = mycon.cursor()

    query = " SELECT id, home_page, examined_pages, complete_crawl FROM records where link_found = 'n' order by id  desc limit 150"   # not in (28, 1, 3, 4, 6, 9, 21, 32, 56) "
    curs.execute(query)

    a = curs.fetchall()
    curs.close()
    mycon.close()

    fi = open("./LOG2", "w")
    sys.stderr = fi

    stats = []
    for row in a:
        id = row[0]
        link = row[1]
        epages = row[2]
        ccrawl = row[3]
        print(id, link)
        print(id, link, file=fi)

        try:
            web = Data(link)
            web.crawl(0.0, 3*epages+50)     # Setting limit as a function of number of pages crawled previously

        except Exception as e:
            print("**** From TESTER ->", e, file=sys.stderr)
            print(file=sys.stderr)

        s, p = get_filters()
        web.get_tsites(s, p)

        print()
        # for i in web.tsites:
        #     print(web.scheme_dom + i)
        # print()

        tmp = []    # will be appended to stats
        tmp.append(id)

        if web.counter <= epages:
            tmp.append(epages)
            tmp.append(ccrawl)
        else:
            tmp.append(web.counter)
            if web.index == len(web.urls):
                tmp.append('y')
            else:
                tmp.append('n')

        tmp2 = []      # 'sites' will be stored in this

        try:
            for li in web.tsites:
                if web.url_file_check(li) == True:  # pdf, ppt, doc, etc. not to be stored -> Only webpagesational institution database
                    # are to be stored
                    tmp2.append(web.scheme_dom+li)
        except Exception as e:
            print("**From crawl_and_find.py Line 72", li)
            print(e, file=sys.stderr)

        if len(tmp2) != 0:
            link_found = 'y'
        else:
            link_found = 'n'

        tmp.append(link_found)
        tmp.append(tmp2)

        stats.append(tmp)


    mycon = connect()
    curs = mycon.cursor()

    for row in stats:
        id = row[0]
        cnt = row[1]
        comple = row[2]
        link_found = row[3]

        query = "UPDATE records SET examined_pages = %s, complete_crawl = '%s', link_found = '%s' WHERE id = %s " %(cnt, comple, link_found, id)
        print(query)
        try:
            curs.execute(query)
            mycon.commit()

        except Exception as e:
            print(query)
            print(e, file=sys.stderr)

        links = row[4]     # for storing in the 'sites' table

        for li in links:
            query = "INSERT INTO sites (id, link) VALUES (%s, '%s')" %(id, li)
            print(query)
            try:
                curs.execute(query)
                mycon.commit()

            except Exception as e:
                print(query)
                print(e, file=sys.stderr)

    fi.close()
    curs.close()
    mycon.close()

