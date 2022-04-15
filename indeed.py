from bs4 import BeautifulSoup
import requests

class indeedScrape():
    def __init__(self, job_title, location, radius, experience):
        self.url = "https://www.indeed.com/jobs?q="+job_title+"&l="+ location+"%2C%20GA&radius="+radius+"&explvl="+experience+"vjk=1a0d0adde0c5fd5d"
    def scrape(self):
        source = requests.get(self.url)
        soup = BeautifulSoup(source.text, "lxml")
        jobs = soup.find_all("h2")
        for i in range(len(jobs)): 
            print(jobs[i])
