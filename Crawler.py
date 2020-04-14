from Extra import *

par=[-1]
pat=['']

class Crawler(Extra):

    __ignored1 = ['.sh']
    __ignored2 = ['.jpg', '.JPG', '.png', '.gif', '.pdf', '.PDF', '.bmp', '.eps', '.deb', '.rpm', '.exe', '.bat', '.mp4', '.doc', '.ppt']
    __ignored3 = ['.jpeg', '.docx', '.bash', '.pptx']
    #
    # __ignored=list()


    def crawl(self):     #calendar to be avoided

        i=0
        while i<len(self.urls):
            try:
                #Don't open a image, pdf, etc. hyperlink

                print(self.urls[i], "->", self.urls[par[i]], pat[i])

                if self.urls[i][-3:] in Crawler.__ignored1 or self.urls[i][-4:] in Crawler.__ignored2 or self.urls[i][-5:] in Crawler.__ignored3:
                    continue

                self.cur_page = self.urls[i]

                soup=BeautifulSoup(load_page(self.urls[i]), 'lxml')

                for t in soup.find_all('a'):

                    if t.has_attr('href')==False:
                        continue
                    path = t['href']
                    try:
                        u = url_normalize(self.cur_page, path)
                    except Exception as e:
                        print(e, self.urls[i], path)

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
                sys.exit()

            finally:
                i+=1


a=''
a=input("Enter URL address: ")

web=Crawler(features='lxml')
web.home_page=a
web.urls.append(a)

web.crawl()

print("\nNo. of URLs =",len(web.urls))
