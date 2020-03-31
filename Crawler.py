from Extra import *

class Crawler(Extra):

    def crawl(self):
        i=0
        try:
            while i<len(self.urls):

                self.cur_page = self.urls[i]
                soup=BeautifulSoup(ur.urlopen(self.urls[i]), 'lxml')


                for t in soup.find_all('a'):
                    path = t['href']

                    u = url_normalize(self.cur_page, path)

                    if u is not None:
                        if target_test(u):
                            if u not in self.tsites:
                                self.tsites.append(u)

                        else:
                            if u not in self.urls:
                                self.urls.append(u)

                i+=1

        except Exception as e:
            print(e, i, self.urls[i])
