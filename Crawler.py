from Extra import *

par=[-1]   #Will later be included in the class itself
pat=['']

class Crawler():

    __ignored1 = ['.sh']
    __ignored2 = ['.jpg', '.JPG', '.png', '.gif', '.pdf', '.PDF', '.bmp', '.eps', '.deb', '.rpm', '.exe', '.bat', '.mp3', '.mp4', '.doc', '.ppt']
    __ignored3 = ['.jpeg', '.JPEG', '.docx', '.bash', '.pptx']
    #
    # __ignored=list()

    def __set_hp(hp):
        if hp=='':
            return None
        else:
            try:
                ht=load_page(hp)
                return ht.geturl()
            except Exception as e:
                print("Error in setting home page", e)
                return ''

    def __init__(self, home_page=''):
        self.home_page=Crawler.__set_hp(home_page)
        self.cur_page=''

        self.urls=list()


        self.tsites=list()
        self.index=-1     #For differentiating between external and internal links

        self.__status=list()
        self.__par=list()  #For tracing back
        self.__pat=list()

        if self.home_page != '':
            self.urls.append(self.home_page)
            self.index=0

    def crawl(self):     #calendar to be avoided

        i=self.index
        while i<len(self.urls):
            try:
                print(self.urls[i], "->", self.urls[par[i]], pat[i])

                if self.urls[i][-3:] in Crawler.__ignored1 or self.urls[i][-4:] in Crawler.__ignored2 or self.urls[i][-5:] in Crawler.__ignored3:
                    continue
                tmp=up.urlparse(self.urls[i])[2]      #Don't open a image, pdf, etc. hyperlink
                if tmp!='':
                    if tmp[-3:] in Crawler.__ignored1 or tmp[-4:] in Crawler.__ignored2 or tmp[-5:] in Crawler.__ignored3:
                        continue

                ht=load_page(self.urls[i])
                #self.urls[i] = ht.geturl()   #If a redirect follows, link in the list not updated as it may result in infinite loop

                if up.urlparse(ht.geturl())[1] != up.urlparse(self.home_page)[1]:   #Redirect to some external link
                    continue

                self.cur_page=ht.geturl()

                soup=BeautifulSoup(ht, 'lxml', parse_only=SoupStrainer('a', attrs={'href':True}))

                for t in soup.find_all('a'):

                    path = t['href']
                    try:
                        u = url_normalize(self.cur_page, path)
                    except Exception as e:
                        print(e, self.urls[i], path)
                    else:
                        if u is not None:
                            if u not in self.urls:
                                self.urls.append(u)
                                par.append(i)
                                pat.append(path)
                time.sleep(0.1)

            except Exception as e:
                print(e, self.urls[i], "**", self.urls[par[i]], pat[i])

            except KeyboardInterrupt:
                print(self.urls[i:])
                print("\nNo. of URLs =", len(web.urls))
                print("No. of pages crawled =", i+1)
                self.index=i
                sys.exit()

            finally:
                i+=1

        self.index=i

    def crawl_page(self):   #Crawls a single page (self.cur_page) and return a list of urls found in that page
        try:
            ht=load_page(self.cur_page)
        except Exception as e:
            print(e)

        else:
            if up.urlparse(ht.geturl())[1] != up.urlparse(self.home_page)[1]:
                print("Redirect to External link")
                return None

            self.cur_page=ht.geturl()

            soup=BeautifulSoup(ht, features='lxml', parse_only=SoupStrainer('a', attrs={'href':True}))

            res=[]

            for t in soup.find_all('a'):
                path=t['href']

                try:
                    u = url_normalize(self.cur_page, path)
                except Exception as e:
                    print(e, self.cur_page, path)
                else:
                    if u is not None:
                        res.append(u)
            return res




a=input("Enter URL address: ")

web=Crawler(a)

web.crawl()

print("\nNo. of URLs =",len(web.urls))
print("No. of pages crawled =", len(web.urls))