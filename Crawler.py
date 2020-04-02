from Extra import *

class Crawler(Extra):

    def crawl(self):

        i=0

        while i<len(self.urls):
            try:
                self.cur_page = self.urls[i]
                soup=BeautifulSoup(load_page(self.urls[i]), 'lxml')

                for t in soup.find_all('a'):
                    path = t['href']

                    u = url_normalize(self.cur_page, path)

                    if u is not None:
                        if u not in self.urls:
                            self.urls.append(u)
                            print(u)

            except Exception as e:
                print(e)

            except KeyboardInterrupt:
                print("\nNo. of URLs =", len(web.urls))
                sys.exit()

            finally:
                i+=1


a='http://jdwcpatna.com'

web=Crawler(features='lxml')
web.home_page=a
web.urls.append(a)

web.crawl()

print("\nNo. of URLs =",len(web.urls))
