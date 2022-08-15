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





# Get web address.
web_address = 'https://polisci.wustl.edu/people/88/all'

# Open website.
web_page = urllib.request.urlopen(web_address)

# soup webpage.
soup = BeautifulSoup(web_page.read())

# Determine what precedes faculty web-page links.
soup.find_all("a")
# Above includes all links, not just faculty web-page links.
soup.find_all('a', {'class' : "card"})
# Above includes just faculty web-page links.

# Find individual faculty members.
all_faculty = soup.find_all("a", {"class" : "card"})
## Each list entry is a faculty member.

# Find each faculty member's personal extension.
fac_ext = []
for i in range(0, len(all_faculty)): # 0 = Dr. Aksoy, 23 = Dr. Rosas.
    fac_ext.append(all_faculty[i]["href"]) # 'href' precedes personal extensions.

# Set pre-extension URL.
pre_ext = 'https://polisci.wustl.edu/people/'

# Make extensions to faculty personal page:
for i in range(0, len(fac_ext)):
    fac_pers = pre_ext + 



