import csv

import requests

from bs4 import BeautifulSoup

url = input("Enter URL to scrap")

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='resultsCol')

indeed_jobs = results.select('div.jobsearch-SerpJobCard.unifiedRow.row.result')

file = open('indeed-jobs.csv', 'w')

writer = csv.writer(file)

# write header rows

writer.writerow(['Title', 'Company', 'Location', 'Apply'])

for indeed_job in indeed_jobs:

   job_title = indeed_job.find('h2', class_='title').text.strip()

   job_company = indeed_job.find('span', class_='company').text.strip()

   job_location = indeed_job.find('span', class_='location accessible-contrast-color-location').text.strip()

   job_url = indeed_job.find('a')['href']

   writer.writerow([job_title.encode('utf-8'), job_company.encode('utf-8'), job_location.encode('utf-8'), job_url.encode('utf-8')])

file.close()
