# Single-threaded Web Crawler

<b>(Front-end part -</b> A compatible Android app is available at https://github.com/Aarya03/Career_Crawler )


This projects includes a single-threaded web crawler. It is designed to crawl sites mainly with content in English or Hindi.
It can handle a variety of MIME types on a website, ignoring links to pdfs, images, zip, docs, etc.

It stores the list of urls found in a website in a Python list. 

Another class Data is for extracting relevant links found in a website. It mainly extracts sites that have some vacancy/job/recruitment related details.

All the sites extracted are stored in MySQL tables.

Additional functionalities include -> (i) logo extractor - to download logo of the organisation whose website is being crawled  
                                      (ii) counter variable - number of pages of a website crawled till now (till KeyboardInterupt)
                                      (iii) a Selenium based web scraper to scrape institutions and their websites


