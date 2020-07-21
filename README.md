# InnovationLab Project - A Web Crawler

This projects includes a single-threaded web crawler. It is designed to crawl mainly sites written in english or hindi.
It can handle a variety of MIME types on a website, ignoring pdfs, images, zip, docs, etc.

It stores the list of urls found in a website in a Python list. 

Another class Data is for extracting relevant links found in a website. It mainly extracts sites that have some vacancy/job/recruitment related details.

All the sites extracted are stored in MySQL tables.

Additional functionalities include -> (i) logo extractor - to download logo of the organisation whose website is being crawled  
                                      (ii) counter variable - number of pages of a website crawled till now (till KeyboardInterupt)
                                      (iii) a Selenium based web scraper to scrape institutions and their websites
