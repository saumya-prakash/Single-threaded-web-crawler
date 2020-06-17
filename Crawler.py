from Extra import *


class Crawler():

    __ignored1 = {'.sh'}
    __ignored2 = {'.csv'}
    __ignored3 = {'.bash'}

    __ignored=set()
    __ignored.union(__ignored1)
    __ignored.union(__ignored2)
    __ignored.union(__ignored3)


    def __set_hp(self, hp):
        if hp=='':
            return
        else:
            try:
                ht=load_page(hp)
                self.home_page = ht.geturl()
                tmp = up.urlparse(self.home_page)
                self.scheme_dom = up.urlunparse((tmp[0], tmp[1], '', '', '', ''))

            except Exception as e:
                print("Error in setting home page", e, file=sys.stderr)
                return

    def __init__(self, home_page):
        self.scheme_dom = ''
        self.home_page=''
        self.cur_page=''
        self.urls=list()
        self.index=-1
        self.__parent=list()  # For tracing back
        self.__path=list()

        self.__set_hp(home_page)

        if self.home_page != '':
            self.urls.append(self.home_page[len(self.scheme_dom):])
            self.__path.append('')
            self.__parent.append(0)
            self.index=0



    def crawl(self, delay=0.0, limiter=-1):     # CALENDAR to be avoided
                        # different counter variable to store no. of pages crawled ?? (wouldn't count the 'non-crawled' pages like pdfs, images, etc.
                        # what if a 'half-link' contains only digits, may belong to some special category, like albums (e.g. https://www.sgei.org/2019/03/ )
        if self.home_page == '':
            print("Nothing to CRAWL")
            return

        i = self.index
        n = len(self.scheme_dom)

        while i < len(self.urls) and i != limiter:
            try:
                print(self.scheme_dom + self.urls[i], "->", self.scheme_dom + self.urls[self.__parent[i]], self.__path[i])

                self.cur_page= self.scheme_dom + self.urls[i]

                for a in self.crawl_page(self.cur_page, delay):
                    if a is not None:
                        if a[0][n:] not in self.urls:
                            self.urls.append(a[0][n:])
                            self.__path.append(a[1])
                            self.__parent.append(i)


            except Exception as e:
                print("**** From Crawler ->", e, file=sys.stderr)
                print(file=sys.stderr)
                print(self.scheme_dom + self.urls[i], "->", self.scheme_dom + self.urls[self.__parent[i]], self.__path[i], file=sys.stderr)


            except KeyboardInterrupt:
                self.index=i
                sys.exit()

            finally:
                i += 1

        self.index=i               # End of function crawl()



    def crawl_page(self, url, delay=0.0):   #Crawls a single page 'url' and yield a list of (url, path) found on that page
        try:
            self.cur_page = url

            if self.url_file_check(url)==False:
                return None

            # if self.url_file_check(up.urlparse(url)[2])==False:       # checking the path part of the URL
            #     return None

            ht=load_page(url)

        except Exception as e:
            print("***From crawl_page() ->", e, file=sys.stderr)

        else:
            if up.urlparse(ht.geturl())[1] != up.urlparse(self.home_page)[1]:
                print("Redirect to an External link")
                return None

            soup=BeautifulSoup(ht, features='lxml', parse_only=SoupStrainer('a', attrs={'href':True}))

            tmp=ht.geturl()

            for t in soup.find_all('a'):
                path=t['href']

                try:
                    u = url_normalize(tmp, path)

                except Exception as e:
                    print("****From url_normalize() ->", e, tmp, path, file=sys.stderr)

                else:
                    if u is not None:
                        yield (u, path)

            time.sleep(delay)


    def get_root(self, u):
        i=0
        for i in range(self.urls):
            if self.urls[i]==u:
                return (self.urls[self.__parent[i]], self.__path[i])

        return None

    def url_file_check(self, s):

        parts = up.urlparse(s)

        if parts[2] =='' and parts[3] == '' and parts[4] == '' and parts[5] == '':    # only 'link' present with no extra components
            return True

                                # checking the complete url
        a = mimetypes.guess_type(s)

        if a[0] is None:
            for i in Crawler.__ignored:
                if s.endswith(i):
                    return False

        elif a[0][0] in {'a', 'c', 'i', 'i', 'm', 'v', 'x'}:
            return False

            # checking the path part of the url
        if parts[2] == '':
            return True

        s = parts[2]

        a = mimetypes.guess_type(s)

        if a[0] is None:
            for i in Crawler.__ignored:
                if s.endswith(i):
                    return False

        elif a[0][0] in {'a', 'c', 'i', 'i', 'm', 'v', 'x'}:
            return False

        return True

if __name__ == '__main__':

    a = Crawler('http://imerpatna.com')

    a.crawl()
    print(a.urls)
