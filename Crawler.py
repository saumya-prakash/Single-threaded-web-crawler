from Extra import *



class Crawler(Extra):

    def crawl(self):

        i=0
        while i<len(self.urls):
            try:     #Don't open a image, pdf hyperlink
                if self.urls[i][-4:] in ['.jpg', '.png', '.gif', '.pdf', '.bmp'] or self.urls[i][-5:] == '.jpeg':
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

                time.sleep(0.5)


            except Exception as e:
                print(e, self.urls[i])

            except KeyboardInterrupt:
                print(self.urls[i:])
                print("\nNo. of URLs =", len(web.urls))
                sys.exit()

            finally:
                i+=1


a='http://www.nitp.ac.in/php/home.php'


web=Crawler(features='lxml')
web.home_page=a
web.urls.append(a)

web.crawl()

print("\nNo. of URLs =",len(web.urls))
