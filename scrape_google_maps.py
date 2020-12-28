# search in order - colleges, universities, educational institutions, research institutions, schools, ...,
# coaching institutions, ..., programming institutes, acting, fine arts, language schools, teacher training
#
# industrial training institutes,
# beauty training, painting, dance, singing, sketching, academy

from selenium import webdriver
import mysql.connector as sqltor
from url_utilities import *


print(datetime.now(), "->", __file__)      # Some utility function to print data-time of run NEEDED

query = input("Enter keyword: ")
# clean 'query' if required
dis = int(input("Enter range (1 - near, 2 - medium, 3 - far): "))

range = '12z'   # default

if dis == 2:
    range = '11z'

elif dis == 3:
    range = '10z'


target = 'https://www.google.com/maps/search/' + query + '+in+patna/@25.5574686,84.9633204,' + range

driver = webdriver.Firefox()
# driver.minimize_window()
driver.get(target)


names = set()

while True:
    time.sleep(60)       # explicit wait of 1 minute to ensure that everything gets loaded
    try:
        soup = BeautifulSoup(driver.page_source, 'lxml')

        for tag in soup.find_all('div', attrs={'class': 'section-result'}):
            try:
                title = tag.find('h3', attrs={'class': 'section-result-title'}).find('span').text
                website = tag.find('a', attrs={'class': 'section-result-action section-result-action-wide'})

                if website is not None:            # if it has a website
                    website = website['href']
                    names.add((title, website))

            except Exception as e:
                print(e)

        a = driver.find_element_by_class_name('n7lv7yjyC35__button-next-icon')     # finding the 'next' button
        a.click()

    except Exception as e:
        print(e)
        break

driver.save_screenshot("./last.png")      # saving the screenshot of the last-visited page
driver.close()

print("Total links found =", len(names))
print()

mycon = sqltor.connect(user='saumya', host='localhost', password='2020', database='project')
curs = mycon.cursor()

for row in names:
    name = row[0]
    home = row[1]

    try:
        if home.startswith('/'):
            home = "https://www.google.com" + home
        ht = load_page(home)
        home = ht.geturl()

        # ???? Avoiding jusdial based home pages ????
        # if bool(re.search('justdial', home, re.IGNORECASE)) == True:
        #     continue

    except Exception as e:
        print(e, name, home)
        print()

    query = "insert into temp (name, home) values ('%s', '%s')" %(name, home)
    try:
        curs.execute(query)
        mycon.commit()
    except Exception as e:
        # print(e)
        pass



curs.close()
mycon.close()

print()