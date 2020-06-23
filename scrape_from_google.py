from url_utilities import *
from db_utilities import *

start = 0
b = set()
for start in range(0, 320):

    try:
        ht = load_page('https://www.google.com/search?client=ubuntu&hs=MLS&sa=X&channel=fs&sz=0&biw=1920&bih=857&q=schools+in+patna&npsic=0&rflfq=1&rlha=0&rllag=25616605,85092215,1401&tbm=lcl&ved=2ahUKEwiLhqeujpjqAhVBX30KHfi6D5oQjGp6BAgMED4&rldoc=1#rlfi=hd:;si:;mv:[[25.669160163970666,85.3535601189149],[25.448635381955807,84.83857598805552]];start:'+str(start))
        soup = BeautifulSoup(ht.read(), features='lxml', parse_only=SoupStrainer('div', attrs={'class':'uMdZh rl-qs-crs-t mnr-c'}))
        ht.close()
    except Exception as e:
        print(e)

    else:
        i = 0
        a = soup.find_all('div', attrs={'class':'uMdZh rl-qs-crs-t mnr-c'})
        n = len(a)

        i = n-1

        while i>=0 and i >= n-20:    # Scraping only the last 20 blocks
            name = a[i].find('div').find('div').find('div').find('div')
            b.add(name.get_text())
            i -= 1

    start += 20

for i in b:
    print(i)

