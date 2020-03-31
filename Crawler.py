from Extra import *

class Crawler(Extra):

    def crawl(self):

        i=0

        while i<len(self.urls):
            try:
                self.cur_page = self.urls[i]
                soup=BeautifulSoup(ur.urlopen(self.urls[i]), 'lxml')

                for t in soup.find_all('a'):
                    path = t['href']

                    u = url_normalize(self.cur_page, path)

                    if u is not None:
                        if u not in self.urls:
                            self.urls.append(u)
                            print(u)
                i+=1


            except Exception as e:
                print(e, self.urls[i])
                print(len(self.urls))
                i+=1


a='https://www.bitmesra.ac.in/BIT_Mesra?cid=8&pid=H'

web=Crawler(ur.urlopen(a), 'lxml')
web.home_page=a
web.urls.append(a)

web.crawl()
