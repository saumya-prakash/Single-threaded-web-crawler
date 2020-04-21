from modules import *
from utilities import *

class Extra(BeautifulSoup):
        home_page=''
        cur_page=''
        urls=list()
        tsites=list()
        index=-1    #for continuing crawling from a particular page
        __status=list()   #for differentiating between INTERNAL links and EXTERNAL links

