# Importing necessary libraries
from bs4 import BeautifulSoup
import requests
import time

# Code for CMD input taken by users
print("Which job position are you looking for?")
job_position = input('>')
print("Name of the location for a given position: ")
job_location = input(">")
print("Write down your skills for related job position: ")
familiar_skill = input('>')
print(f'Filtering out {familiar_skill}')

# Function to find jobs
def find_jobs():
    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_position}&txtLocation={job_location}"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"html.parser")
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx') # job posting lists
    
    for index, job in enumerate(jobs): # enumerating to index along with job content
        published_date = job.find('span',class_='sim-posted').span.text # published date
        if 'few' in published_date:
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','') 
            skills = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info =job.header.h2.a['href']
            if familiar_skill in skills: # filtering results based on given skills by the user
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')

# Driver Code     
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} minutes...')
        time.sleep(time_wait*60) # wait certain amount of time
        
        # Check the posts directory to find txt files of your results