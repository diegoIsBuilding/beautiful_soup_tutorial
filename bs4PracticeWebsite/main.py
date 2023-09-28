#import Beautiful Soup
#import requests

from bs4 import BeautifulSoup
import requests
import time

print('Add skills you are not familiar with')
#Filter Unfamiliar Skills
unfamilar_skill = input('>')
print(f'Filtering out {unfamilar_skill}')

def find_jobs():
    url = 'https://tinyurl.com/2x4ry2e4'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #print(jobs)
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', 
            class_ = 'joblist-comp-name').text.replace(' ', '')
            key_skills = job.find('span', 
            class_ = 'srp-skills').text.replace(' ','')
            #key_skills_list = key_skills.split(',')
            #print(key_skills_list)
            more_info = job.header.h2.a['href']
            if unfamilar_skill not in key_skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {key_skills.strip()} \n')
                    f.write(more_info)
                print(f'File saved: {index}')
            
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)    
#Challenge
#Create a list of unfamiliar skill inputs and check that list against a list of skills required
#make sure to clean the required skills list to make sure that input match properly 