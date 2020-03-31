from bs4 import BeautifulSoup
import re
import lxml
import os
import sys
import urllib.request as ur
import urllib.parse as up


class Extra(BeautifulSoup):
    def __init__(self, hpage, curpage):
        self.home_page=hpage
        self.cur_page=curpage
        self.urls=[hpage]
        self.tsites=list()