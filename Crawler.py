from Extra import *

# par=[0]   #Will later be included in the class itself
# pat=['']

class Crawler():

    __ignored1 = {'.sh'}     #Use if mimetypes module seems inevitable
    __ignored2 = {'.m4a', '.rar', '.jpg', '.JPG', '.png', '.gif', '.pdf', '.PDF', '.bmp', '.eps', '.deb', '.rpm', '.exe', '.bat', '.mp3', '.mp4', '.doc', '.ppt', '.xls', '.csv'}
    __ignored3 = {'.jpeg', '.JPEG', '.docx', '.bash', '.pptx', '.xlsx', '.json'}
    #
    # __ignored=list()

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
                print("Error in setting home page", e)
                return


    def __init__(self, home_page):
        self.scheme_dom = ''
        self.home_page=''
        self.cur_page=''
        self.urls=list()
        self.index=-1     #For differentiating between external and internal links
        self.__status=list()
        self.__par=[0]  #For tracing back
        self.__pat=['']

        self.__set_hp(home_page)


        if self.home_page != '':
            self.urls.append(self.home_page[len(self.scheme_dom):])
            self.index=0



    def crawl(self, delay=0.0):     #CALENDAR to be avoided

        if self.home_page=='':
            print("Nothing to CRAWL")
            return

        i=self.index
        n=len(self.scheme_dom)

        while i<len(self.urls):
            try:
                print(self.scheme_dom + self.urls[i], "->", self.scheme_dom + self.urls[self.__par[i]], self.__pat[i])

                self.cur_page= self.scheme_dom + self.urls[i]

                for a in self.crawl_page(delay):
                    if a is not None:
                        if a[0][n:] not in self.urls:
                            self.urls.append(a[0][n:])
                            self.__par.append(i)
                            self.__pat.append(a[1])


                # if self.urls[i][-3:] in Crawler.__ignored1 or self.urls[i][-4:] in Crawler.__ignored2 or self.urls[i][-5:] in Crawler.__ignored3:
                #     continue
                # tmp=up.urlparse(self.urls[i])[2]      #Don't open a image, pdf, etc. hyperlink
                # if tmp!='':
                #     if tmp[-3:] in Crawler.__ignored1 or tmp[-4:] in Crawler.__ignored2 or tmp[-5:] in Crawler.__ignored3:
                #         continue
                #
                # ht=load_page(self.urls[i])
                # #self.urls[i] = ht.geturl()   #If a redirect follows, link in the list not updated as it may result in infinite loop
                #
                # if up.urlparse(ht.geturl())[1] != up.urlparse(self.home_page)[1]:   #Redirect to some external link
                #     continue
                #
                # self.cur_page=ht.geturl()
                #
                # soup=BeautifulSoup(ht, 'lxml', parse_only=SoupStrainer('a', attrs={'href':True}))
                #
                # for t in soup.find_all('a'):
                #
                #     path = t['href']
                #     try:
                #         u = url_normalize(self.cur_page, path)
                #     except Exception as e:
                #         print(e, self.cur_page, path)
                #     else:
                #         if u is not None:
                #             if u not in self.urls:
                #                 self.urls.append(u)
                #                 self.__par.append(i)
                #                 self.__pat.append(path)
                # time.sleep(delay)

            except Exception as e:
                print(e, self.urls[i], "**")

            except KeyboardInterrupt:
                self.index=i
                print("No. of urls =", len(self.urls))
                print("No. of urls crawled =", i+1)
                return


            finally:
                i+=1

        self.index=i



    def crawl_page(self, delay=0.0):   #Crawls a single page (self.cur_page) and return a list of urls found in that page
        try:
            url = self.cur_page

            if url[-3:] in Crawler.__ignored1 or url[-4:] in Crawler.__ignored2 or url[-5:] in Crawler.__ignored3:
                return None
            tmp = up.urlparse(url)[2]  # Don't open a image, pdf, etc. hyperlink
            if tmp != '':
                if url[-3:] in Crawler.__ignored1 or url[-4:] in Crawler.__ignored2 or url[-5:] in Crawler.__ignored3:
                    return None

            ht=load_page(url)

        except Exception as e:
            print(e)

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
                    print(e, tmp, path)
                else:
                    if u is not None:
                        yield (u, path)

            time.sleep(delay)


    def get_root(self, u):
        i=0
        for i in range(self.urls):
            if self.urls[i]==u:
                return (self.urls[self.__par[i]], self.__pat[i])

        return None




