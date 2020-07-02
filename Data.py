from Crawler import *

class Data(Crawler):

    def __init__(self, homepage):
        super().__init__(homepage)
        self.tsites=list()

    def get_tsites(self, a, b=[]):

        for link in self.urls:      # Examining every link ('half' link) present in the urls[]

            for i in b:    # Negative filter
                if bool( re.search(i, link, re.IGNORECASE) ) == True:
                    break
            else:
                for j in a:
                    if bool( re.search(j, link, re.IGNORECASE) ) == True:
                        self.tsites.append(link)
                        break



    def get_logo(self):

        def img_to_hpage(tag):
            if tag.name != 'a':
                return False

            if tag.has_attr('href') == False:  # <a> tag has no href attribute
                return False


            c = tag.find('img')
            if c is None:  # no <img> tag inside the given <a> tag
                return False

            p = tag['href']
            q = url_normalize(self.home_page, p)

            if q != self.home_page:
                return False

            return True

        def src_or_alt(tag):
            if tag.name != 'img':
                return False

            if tag.has_attr('src'):
                if bool(re.search('logo', tag['src'], re.IGNORECASE)) == True:
                    return True

            if tag.has_attr('alt'):
                if bool(re.search('logo', tag['alt'], re.IGNORECASE)) == True:
                    return True

            return False

        ht = load_page(self.home_page)
        soup = BeautifulSoup(ht, features='lxml', parse_only=SoupStrainer(['img', 'a']))

        a = ['title', 'id', 'class']       # attributes to be checked

        t = None

        if t is None:                # link to the home-page heuristic
            t = soup.find(img_to_hpage)

        if t is None:
            t = soup.find(src_or_alt)       # 'src' and 'alt' are at the highest priority level

        if t is None:
            for key in a:       # searching for appropriate <img> tag with 'logo' keyword
                t = soup.find('img', attrs={key : re.compile('logo', re.IGNORECASE)})
                if t is not None:
                    break


        if t is None:           # searching for appropriate <img> tag with 'banner' keyword
            for key in a:
                t = soup.find('img', attrs={key : re.compile('banner', re.IGNORECASE)})
                if t is not None:
                    break

        if t is None:           # searching for appropriate <img> tag with 'header' keyword ------>   EXPERIMENTAL
            for key in a:
                t = soup.find('img', attrs={key : re.compile('header', re.IGNORECASE)})
                if t is not None:
                    break

        # 'image' keyword can also be tried

        if t is None:
            # print("Logo couldn't be found")
            return None

        u = None
        if t.name == 'img':
            u = url_normalize(self.home_page, t['src'])

        else:
            t = t.find('img')
            u = url_normalize(self.home_page, t['src'])

        if u is None:
            u = t['src']
            u = url_normalize(u, u)    # normalizing 'u' just in case it contains some control characters

        # print(u)
        # print("Logo Found")
        return load_page(u)      # to bypass 'forbidden' error



    def __get_from_table(self, tag, cur_url):
        if tag is None:
            return

        for row in tag.find_all('tr'):       # examining every row
            a = row.find('a')

            if a is None or a.has_attr('href') == False:
                continue

            link = url_normalize(cur_url, a['href'])
            if link is None:
                continue

            ht = load_page(link)
            res_headers = ht.info()
            l_modified = res_headers.get_all('last-modified')

            if self.check_for_download(a['href']):  # good for downloading

                if cmp_date(l_modified, 120):  # recent document found -> save it
                    name = a.stripped_strings.replace('/', ' ')  # substituting '/' with ' '
                    with open(name, "wb") as fi:  # any type of file (simple text or binary) saved through 'wb' mode
                        fi.write(ht.read())

            else:     # not good for downloading -> some link to other page or other thing
                with open('additional_links', 'a') as fi:          # last-modified not checked - assuming it won't be very useful in this case (REVIEW LATER)
                    fi.write(name+' ')
                    fi.write(link+'\n')



    def __get_from_form(self, tag, cur_url):
        if tag is None:
            return

        pass


    def download_data(self, url):
        soup = BeautifulSoup(load_page(url), features='lxml')

        tag=None
        tag = soup.find('table')   # searching for <table> tag
        self.__get_from_table(tag, url)

        tag = None
        tag = soup.find('form')      # searching for <form> tag
        self.__get_from_form(tag, url)

                                    # check_for_download only checks on the basis of the url ; 'content-type' header should also be used
    def check_for_download(self, s):    # if the file can be downloaded (image, pdf, doc, sheet, etc.)

                                        # checking the complete 'href' attribute
        a = mimetypes.guess_type(s)
        a = a[0]

        if a is not None:
            if a.startswith('application/'):
                appli = ['pdf', 'csv', 'json', 'msword', 'vnd.openxmlformats-officedocument.wordprocessingml.document',
                         'vnd.ms-excel', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                         'vnd.oasis.opendocument.text', 'vnd.oasis.opendocument.presentation', 'vnd.oasis.opendocument.spreadsheet']
                # types = [.pdf .csv .json .doc .docx .xls .xlsx .odt .odp .ods ]

                if a[12:] in appli:
                    return True

            if a == 'text/plain':
                return True

            if a.startswith('image'):
                return True
                                # checking the path part of the 'href' attribute
        s = up.urlparse(s)
        s = s[2]

        if s == '':
            return False

        a = mimetypes.guess_type(s)
        a = a[0]

        if a is None:
            return False

        if a.startswith('application/'):
            appli = ['pdf', 'csv', 'json', 'msword', 'vnd.openxmlformats-officedocument.wordprocessingml.document',
                     'vnd.ms-excel', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     'vnd.oasis.opendocument.text', 'vnd.oasis.opendocument.presentation',
                     'vnd.oasis.opendocument.spreadsheet']
            # types = [.pdf .csv .json .doc .docx .xls .xlsx .odt .odp .ods ]

            if a[12:] in appli:
                return True

        if a == 'text/plain':
            return True

        if a.startswith('image'):
            return True

        return False






if __name__ == '__main__':

    a = input("Enter URL address: ")
    b = float(input("Input delay: "))

    web = Data(a)

    # fi = open("/home/saumya/Desktop/single_log", "w")
    # sys.stderr = fi

    # image = web.get_logo()
    # print(image)
    web.crawl(b, 100000)


    print("\nNo. of URLs =", len(web.urls))
    print("No. of pages examined =", web.counter)

    s, p = get_filters()

    web.get_tsites(s, p)

    for i in web.tsites:
        print(i)

    # fi.close()


