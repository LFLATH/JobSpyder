from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests

class indeedScrape():
    def __init__(self, job_title, location, radius, experience):
        self.url = "https://www.indeed.com/jobs?q="+job_title+"&l="+ location+"&radius="+radius+"&explvl="+experience
    def createLinks(self, links):
        for link in links:
            print("https://www.indeed.com"+link)
    def cleanLinks(self, links):
        useful_urls = []
        for link in links:
            if "pagead" in str(link):
                useful_urls.append(str(link))
        self.createLinks(useful_urls)
    def scrape(self):
        scraped_links = []
        source = requests.get(self.url)
        for link in BeautifulSoup(source.text,'html.parser', parse_only = SoupStrainer('a')):
            if link.has_attr('href'):
                  scraped_links.append(link['href'])
        self.cleanLinks(scraped_links)
