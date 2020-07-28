import requests
from bs4 import BeautifulSoup

URL = 'https://www.indeed.com/jobs?q=software+developer&l=California&explvl=entry_level'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsCol')

def printJobs(div, title, company, location):
    job_elems = results.find_all('div', class_=div)
    for job_elem in job_elems:
        title_elem = job_elem.find(title, class_='title')
        company_elem = job_elem.find(company, class_='company')
        location_elem = job_elem.find(location, class_='location accessible-contrast-color-location')
        if None in (title_elem, company_elem, location_elem):
            continue
        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print()

searchCard = 'jobsearch-SerpJobCard unifiedRow row result'
printJobs(searchCard, 'h2', 'span', 'div')
printJobs(searchCard, 'h2', 'span', 'span')

searchCard = 'jobsearch-SerpJobCard unifiedRow row result clickcard'
printJobs(searchCard, 'h2', 'span', 'div')
printJobs(searchCard, 'h2', 'span', 'span')



