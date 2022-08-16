## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization 
##  	Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##		Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence. 
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import urllib.request
import csv 
import random
import time


# Most important information should be available from faculty personal websites.

# STRATEGY:
#   1. Figure out way to access faculty-specific web-pages.
#   2. Figure out way to gather all relevant info from example faculty (like Deniz Aksoy)
#   3. Replicate this process for all faculty.
#   4. Place into csv file.
    

# STEP 1. Figure out way to access faculty-specific webpages.

# Create reference object for, open, and soup overall website.
web_address = 'https://polisci.wustl.edu/people/88/all'
web_page = urllib.request.urlopen(web_address)
soup = BeautifulSoup(web_page.read())
# View how tags are nested in the document.
print(soup.prettify())
#   NOTE: 'a' tags seem to contain links, including faculty-specific URL extensions.
# Find all instances of 'a' tag.
soup.find_all("a")
# Extract all elements with the 'a' tag.
atags = soup.find_all('a')
# Inspect the attributes of one element of the 'a' tag.
atags[19].attrs # Deniz Aksoy's a-tag.
#   NOTE: the attribute 'href' contains faculty's personal extensions.
atags[19]['href']
# NEW GOAL: limit to only atags associated with faculty.
# See if non-faculty a-tags have 'class' attribute.
for i in range(0, len(atags) - 1):
    print(atags[i])
# We need to extract class and href data
# Create dictionary with lists for both of these.
l = {"class" : [], "href" : []} # create a dictionary
for p in range(0, len(atags) - 1):
    try:
        # extract all attrs 'class' from the all_a_tags
        l["class"].append(atags[p].attrs["class"])
    except:
        l["class"].append(None)
        # extract all attrs 'href' from the all_a_tags
    try:
        l["href"].append(atags[p].attrs["href"])
    except:
        l["href"].append(None)
print(l)
# Figure out what class attributes correspond to faculty.
for i in range(0, len(atags) - 1):
    print(f"{i}. {l['href'][i]}  {l['class'][i]}\n")
# 'card' corresponds to faculty.
atags2 = atags[19:44]
l = {"class" : [], "href" : []} # create a dictionary
for p in range(0, len(atags2) - 1):
    try:
        # extract all attrs 'class' from the all_a_tags
        l["class"].append(atags2[p].attrs["class"])
    except:
        l["class"].append(None)
        # extract all attrs 'href' from the all_a_tags
    try:
        l["href"].append(atags2[p].attrs["href"])
    except:
        l["href"].append(None)
for i in range(0, len(atags2) - 1):
    print(f"{i}. {l['href'][i]}  {l['class'][i]}\n")
# Now only faculty are let.
# Extract faculty homepage links.
preext = 'https://polisci.wustl.edu'
fac_pers = []
for i in range(0, len(atags2) - 1):
    fac_pers.append(preext + atags2[i]["href"])
 
    
# STEP 2. Figure out way to gather all relevant info from example faculty (like Deniz Aksoy)

# Open personal page.
inner_page = urllib.request.urlopen(fac_pers[0])
# Soup personal page.
inner_soup = BeautifulSoup(inner_page.read())
## NEEDED FIELDS: Specialization, Name, Title, E-mail, Web page
# Web-pages. FINISHED
fac_pers
# Name. FINISHED
inner_soup.find("h1").text
# Title. FINISHED
inner_soup.find("div", {"class" : "title"}).text
# Email. FINISHED
inner_soup.find("ul", {"class" : "detail contact"}).find("a").text
# Specialization. FINISHED.
inner_soup.find("div", {"class" : "post-excerpt"}).text


# STEP 3: Replicate process for all faculty.

# Keep only those with faculty.
all_faculty = soup.find_all("a", {"class": "card"})
preext = 'https://polisci.wustl.edu'
for i in range(0, len(all_faculty) - 1):
    try:
        professor = {}
        professor_i = all_faculty[i]
        
        # Webpages.
        professor["webpage"] = preext + professor_i["href"]
        
        inner_page_url = preext + professor_i["href"]
        inner_page = urllib.request.urlopen(inner_page_url)
        inner_soup = BeautifulSoup(inner_page.read())
        
        # Name.
        professor["name"] = inner_soup.find("h1").text
        
        # Title.
        professor["title"] = inner_soup.find("div", {"class" : "title"}).text
        
        # Email.
        professor["email"] = inner_soup.find("ul", {"class" : "detail contact"}).find("a").text
        
        # Specialization.
        professor["specialization"] = inner_soup.find("div", {"class" : "post-excerpt"}).text
    except:
        professor["name"] = "NA"
        professor["title"] = "NA"
        professor["email"] = "NA"
        professor["specialization"] = "NA"


# STEP 4: Place into CSV file.

from bs4 import BeautifulSoup
import urllib.request
import csv 
import random
import time

with open('washu_faculty.csv', 'w') as f:
    # Define column names.
    w = csv.DictWriter(f, fieldnames = ("webpage", "name", "title", "email", "specialization"))
    # Write header.
    w.writeheader()
    web_address = 'https://polisci.wustl.edu/people/88/all'
    web_page = urllib.request.urlopen(web_address)
    soup = BeautifulSoup(web_page.read())
    all_faculty = soup.find_all("a", {"class": "card"})
    preext = 'https://polisci.wustl.edu'
    counter = 0
    for i in all_faculty:
        counter += 1
        print("Working on " + str(counter) + " of " + str(len(all_faculty)))
        professor = {}
        professor_i = all_faculty[i].find_all("href")
        
        # Webpages.
        professor["webpage"] = preext + professor_i["href"]

        inner_page_url = preext + professor_i["href"]
        inner_page = urllib.request.urlopen(inner_page_url)
        inner_soup = BeautifulSoup(inner_page.read())
            
        # Name.
        try:
            professor["name"] = inner_soup.find("h1").text
        except:
            professor["name"] = "NA"
        
        # Title.
        try:
            professor["title"] = inner_soup.find("div", {"class" : "title"}).text
        except:
            professor["title"] = "NA"
           
        # Email.
        try:
            professor["email"] = inner_soup.find("ul", {"class" : "detail contact"}).find("a").text
        except:
            professor["email"] = "NA"
           
        # Specialization.
        try:
            professor["specialization"] = inner_soup.find("div", {"class" : "post-excerpt"}).text
        except:
            professor["specialization"] = "NA"
            
        # Write the row in the csv file for this specific faculty member.
        w.writerow(professor)
        # Allow for some sleeping so you don't DDOS website.
        time.sleep(random.uniform(1, 5))
print("FINISHED!")

with open("washu_faculty.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(prof_info.keys())
    writer.writerows(zip(*prof_info.values()))



# Check contents of csv file.
with open('washu_faculty.csv', 'r') as f:
  my_reader = csv.DictReader(f)
  for row in my_reader:
    print(row)

