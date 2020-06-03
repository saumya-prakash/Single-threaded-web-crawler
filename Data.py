from Extra import *
from Crawler import Crawler

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

        ht=load_page(self.home_page)

        soup = BeautifulSoup(ht, features='lxml', parse_only=SoupStrainer('img'))

        a = ['src', 'alt', 'title', 'id']
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

        ur.urlretrieve(u, 'logo')
        print("logo downloaded")


    def download_data(self):
        for i in self.tsites:
            for link in self.crawl(self.scheme_dom + i, 0):      # examining each found link and downloading it if it is a pdf, image, etc.
                pass




a=input("Enter URL address: ")
b=float(input("Input delay: "))

web=Data(a)

web.get_logo()

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



