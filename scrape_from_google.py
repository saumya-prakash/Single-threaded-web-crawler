import time
from selenium import webdriver
from bs4 import BeautifulSoup
import mysql.connector as sqltor

driver = webdriver.Firefox()
driver.minimize_window()
driver.get('https://www.google.com/maps/search/educational+institutions+in+patna/@25.5574686,84.9633204,12z')

names = set()

while True:
    time.sleep(10)
    try:
        soup = BeautifulSoup(driver.page_source, 'lxml')

        for tag in soup.find_all('div', attrs={'class': 'section-result'}):
            try:
                title = tag.find('h3', attrs={'class': 'section-result-title'}).find('span').text
                website = tag.find('a', attrs={'class': 'section-result-action section-result-action-wide'})

                if website is not None:
                    website = website['href']
                    names.add((title, website))

            except Exception as e:
                print(e)

        a = driver.find_element_by_class_name('n7lv7yjyC35__button-next-icon')
        a.click()

    except Exception as e:
        print(e)
        break

driver.save_screenshot("./last.png")
driver.close()

mycon = sqltor.connect(user='saumya', host='localhost', password='2020', database='project')
curs = mycon.cursor()

for row in names:
    name = row[0]
    home = row[1]
    # print(name, home)
    query = "insert into temp (name, home) values ('%s', '%s')" %(name, home)
    try:
        curs.execute(query)
    except Exception as e:
        # print(e)
        pass

mycon.commit()

curs.close()
mycon.close()