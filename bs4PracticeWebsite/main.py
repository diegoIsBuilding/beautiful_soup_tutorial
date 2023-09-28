#import Beautiful Soup
#import requests

from bs4 import BeautifulSoup
import requests


url = 'https://tinyurl.com/2x4ry2e4'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
#print(jobs)
for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', 
        class_ = 'joblist-comp-name').text.replace(' ', '')
        key_skills = job.find('span', 
        class_ = 'srp-skills').text.replace(' ','')
#print(published_date)

    print(f'''
          Company Name: {company_name}
          Skills Required: {key_skills}
          ''')