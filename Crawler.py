from Extra import *


class Crawler(Extra):

    def crawl(self):

        i=0
        while i<len(self.urls):
            try:
                #Don't open a image, pdf, etc. hyperlink

                ignored1=['.sh']
                ignored2=['.jpg', '.png', '.gif', '.pdf', '.bmp', '.eps', '.deb', '.rpm', '.exe', '.bat']
                ignored3=['.jpeg']

                if self.urls[i] in ignored1 or self.urls[i][-4:] in ignored2 or self.urls[i][-5:] in ignored3:
                    continue

                self.cur_page = self.urls[i]

                soup=BeautifulSoup(load_page(self.urls[i]), 'lxml')


                for t in soup.find_all('a'):

                    if t.has_attr('href')==False:
                        continue

                    path = t['href']
                    u = url_normalize(self.cur_page, path)

                    if u is not None:
                        if u not in self.urls:
                            self.urls.append(u)
                            print(u)


            except Exception as e:
                print(e, self.urls[i])

            except KeyboardInterrupt:
                print(self.urls[i:])
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
