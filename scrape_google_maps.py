from selenium import webdriver

import mysql.connector as sqltor
from url_utilities import *

driver = webdriver.Firefox()
driver.minimize_window()
driver.get('https://www.google.com/maps/search/play+schools+in+patna/@25.5574686,84.9633204,12z')
# search in order - colleges, universities, educational institutions, research institutions, schools, ..., coaching institutions, ..., programming institutes, industrial training institutes,

names = set()

while True:
    time.sleep(60)       # explicit wait, so that everything gets loaded
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

driver.save_screenshot("./last.png")
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

    except Exception as e:
        print(e, name, home)

    query = "insert into temp (name, home) values ('%s', '%s')" %(name, home)
    try:
        curs.execute(query)
    except Exception as e:
        # print(e)
        pass

mycon.commit()

curs.close()
mycon.close()