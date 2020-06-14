from Crawler import *

class Data(Crawler):

    def __init__(self, homepage):
        super().__init__(homepage)
        self.tsites=list()

    def get_tsites(self, a, b=[]):

        for link in self.urls:

            for i in b:   #Negative filter
                if bool(i.search(link)):
                    break
            else:
                for j in a:
                    if bool(j.search(link)):
                        self.tsites.append(link)
                        break


    def __img_hpage(self, tag):
        if tag.name != 'a':
            return False

        if tag.has_attr('href') == False:     # <a> tag has no href attribute
            return False

        a = None
        a = tag.find('img')
        if a is None:       # no <img> tag inside the given <a> tag
            return False

        path = tag['href']
        u = url_normalize(self.home_page, path)

        if u != self.home_page:
            return False

        return True


    def get_logo(self):

        ht = load_page(self.home_page)

        soup = BeautifulSoup(ht, features='lxml', parse_only=SoupStrainer('img'))

        a = ['src', 'alt', 'title', 'id', 'class']
        t = None

        for key in a:       # searching for appropriate <img> tag with 'logo' keyword
            t = soup.find('img', attrs={key : re.compile('logo', re.IGNORECASE)})
            if t is not None:
                break

        if t is None:                # link to the home-page heuristic
            soup2 = BeautifulSoup(ht, features='lxml', parse_only=SoupStrainer('a'))
            t = soup2.find(self.__img_hpage)

        if t is None:           # searching for appropriate <img> tag with 'banner' keyword
            for key in a:
                t = soup.find('img', attrs={key : re.compile('banner', re.IGNORECASE)})
                if t is not None:
                    break

        if t is None:
            print("Logo couldn't be found.")
            return

        if t.name == 'img':
            u = url_normalize(self.home_page, t['src'])

        else:
            t = t.find('img')
            u = url_normalize(self.home_page, t['src'])

        if u is None:
            u = t['src']

        ht = load_page(u)      # to bypass 'forbidden' error

        with open("aaa_logo", "wb") as file:
            file.write(ht.read())
        print("logo downloaded")

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

            if cmp_date(l_modified, 120):     # recent document found -> save it
                name = ' '.join(a.stripped_strings)
                k=0
                while name[k] != '/':         # name of the resource (with '/' removed)
                    k += 1
                name = name[0:k]

                print(name)

                if self.check_for_download(a['href']):  # good for downloading
                    with open(name, "wb") as fi:    # any type of file (simple text or binary) saved through 'wb' mode
                        fi.write(ht.read())

                else:     # not good for downloading -> some link to other page or other thing
                    with open('additional_links', 'a') as fi:
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


    def check_for_download(self, s):    # if the file can be downloaded (image, pdf, doc, sheet, etc.)
        a = mimetypes.guess_type(s)
        a = a[0]

        if a[0:12] == 'application/':
            appli = ['pdf', 'csv', 'json', 'msword', 'vnd.openxmlformats-officedocument.wordprocessingml.document',
                     'vnd.ms-excel', 'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     'vnd.oasis.opendocument.text', 'vnd.oasis.opendocument.presentation', 'vnd.oasis.opendocument.spreadsheet']
            # types = [.pdf .csv .json .doc .docx .xls .xlsx .odt .odp .ods ]

            if a[12:] in appli:
                return True

        if a=='text/plain':
            return True

        if a[0:5]=='image':
            return True

        return False






if __name__ == '__main__':


    a=input("Enter URL address: ")
    b=float(input("Input delay: "))

    web=Data(a)

    # web.get_logo()
    # web.crawl(b)

    print("\nNo. of URLs =", len(web.urls))
    print("No. of pages crawled =", web.index)


    s=[]
    p=[]

    s.append(re.compile('vacanc', re.IGNORECASE))
    s.append(re.compile('job', re.IGNORECASE))
    s.append(re.compile('career', re.IGNORECASE))
    s.append(re.compile('opportunit', re.IGNORECASE))
    # s.append(re.compile('notice', re.IGNORECASE))   #Very generous filter
    # s.append(re.compile('announcement', re.IGNORECASE))
    s.append(re.compile('recruit(?!er(s)?)', re.IGNORECASE))
    s.append(re.compile('position', re.IGNORECASE))
    s.append(re.compile('role', re.IGNORECASE))
    s.append(re.compile('walk( )?(-)?( )?in', re.IGNORECASE))
    s.append(re.compile('interview', re.IGNORECASE))

    p.append(re.compile('result', re.IGNORECASE))


    web.get_tsites(s, p)

    for i in web.tsites:
        print(i)



