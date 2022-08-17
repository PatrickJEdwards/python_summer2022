# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 21:24:04 2022

@author: edwar
"""

#%%
# Preliminaries.
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import os

os.chdir('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\HW')

# GOAL/INSTRUCTIONS: 
##   Unit of Analysis (Rows) - All Biden's spoken addresses since 2021-01-20.
##   Information (Columns):
##       1. Date of spoken address.
##       2. Title.
##       3. Full text of address/remarks.
##       4. Citation/Footnote (if one exists)
##   SLEEP after accessing each document.

# STRATEGY - OVERALL:
##  There have been 623 remarks (I think) since Biden's inaugural speech.
##  So, set 625 remarks/page using '?items_per_page=60' in URL.
##  Alternatively, I could ensure page # using '&page=3' in URL (after remarks/page part of URL)
##  SEARCH PAGE:
###     Only use speeches by Joe Biden.
###     Collect speech date.
###     Collect speech title.
## SPEECH PAGE:
###     Collect full text of address/remark.
###     Collect citation/footnote (if one exists)
## Go page by page until January 20 2020. (pg. 11 if 60 results/page).

# STRATEGY - SPECIFIC STEPS:
## STEP 1: Gain my bearings.
###     1A. Access website.
###     1B. Isolate html element corresponding to individual speeches.
###     1C. Isolate only Biden speeches, skip other authors.
## STEP 2: Get Information
###     2A. Define framework that accumulates info.
###     2B. Collect 'Date of Spoken Address' information.
###     2C. Collect 'Title' information.
###     2D. Access actual remark page.
###     2E. Collect 'full text of address/remarks' information.
###     2F. Collect 'citation/footnote' information, if it exists.
## STEP 3: Completeness checks.
###     3A. Ensure that search stops at January 20, 2020.
###     3B. Ensure search goes through entire archive.
###     3C. INCLUDE SLEEP FUNCTIONALITY.
## STEP 4: Create CSV file of data.


#%%
# Homework #2 Answer.

# Preliminaries.
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import os
import random
import time

# Actual csv input.
with open("HW02_Answers.csv", "w", newline='') as f:
    w = csv.DictWriter(f, fieldnames = ("date", "title", "text", "citation", "footnote"))
    w.writeheader()
    # Create correct URL with 625 speeches.
    web_address = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks"
    items_per_page = "?items_per_page="
    goal_url = web_address + items_per_page + "625"
    del web_address
    del items_per_page
    # open and parse website.
    web_page = urllib.request.urlopen(goal_url)
    del goal_url
    soup = BeautifulSoup(web_page.read())
    del web_page
    # Isolate individual remarks.
    divtags = soup.find_all("div", {"class" : "views-row"})
    del soup
    # Isolate only speeches with Biden as author.
    all_remarks = []
    for i in divtags:
        if "Biden" in i.find_all("a")[1].text:
            all_remarks.append(i)
        else:
            pass
    del divtags
    # Create counter.
    counter = 0
    # Create initial (pre-extension) part of URL.
    pre_URL = "https://www.presidency.ucsb.edu"
    
##### Generate for-loop for finding data.
    for i in all_remarks:
        # Update counter.
        counter += 1
######### Print update using counter.
        print("Working on " + str(counter) + " of " + str(len(all_remarks)))
        # Create empty dictionary to fill in.
        remark = {}
        # Find extension to remarks personal page.
        extension = i.find_all("div", {"class" : "field-title"})[0].find_all("a")[0]["href"]
        
###     2B. Collect 'Date of Spoken Address' information.
        remark["date"] = i.find("span", {"class" : "date-display-single"}).text
    
###     2C. Collect 'Title' information.
        remark["title"] = i.find("div", {"class" : "field-title"}).text[1:]

###     2D. Access actual remark page.
        try:
            remark_page = urllib.request.urlopen(pre_URL + extension)
        except urllib.error.URLError:
            remark["text"] = "NA"
            remark["citation"] = "NA"
            w.writerow(remark)
            continue
        remark_html = BeautifulSoup(remark_page.read())
        
###     2E. Collect 'full text of address/remarks' information.
        remark["text"] = remark_html.find_all("div", {"class" : "field-docs-content"})[0].text[1:]


###     2F. Collect 'citation/footnote' information, if it exists.
        try:
            remark["citation"] = remark_html.find_all("div", {"class" : "field-prez-document-citation"})[0].text[1:]
        except:
            remark["citation"] = "NA"
            continue
        try:
            remark["footnote"] = remark_html.find_all("div", {"class" : "field-docs-footnote"})[0].text
        except:
            remark["footnote"] = "NA"
            continue
        w.writerow(remark)
        time.sleep(random.uniform(1, 3)) # be polite, sleep!
print("ALL DONE!")

















#%%
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.
### IGNORE EVERYTHING BELOW THIS.

















#t_extension = test_remarks[17].find_all("div", {"class" : "field-title"})[0].find_all("a")[0]["href"]
#t_remark_page = urllib.request.urlopen(pre_URL + t_extension)
#t_remark_html = BeautifulSoup(t_remark_page.read())

# Text.
#t_text = t_remark_html.find_all("div", {"class" : "field-docs-content"})[0].text[1:]
#t_text

#preprocessed_text = t_remark_html.find_all("div", {"class" : "field-docs-content"})[0].text[1:]
#processed_text = preprocessed_text.replace("—","-").replace("–","-")
#processed_text


# citation.
#t_remark_html.find_all("div", {"class" : "field-prez-document-citation"})[0].text[1:]
#    "p", {"class" : "ucsbapp_citation"})[0].text

# footnote.
#t_remark_html.find_all("div", {"class" : "field-docs-footnote"})[0].text[1:]





#%%
## STEP 1: Gain my bearings.

###     1A. Access website.

# Create string for website.
web_address = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks"
# Create string for including 60 remarks on each page.
items_per_page = "?items_per_page="
# [NO LONGER NECESSARY] Create string for page number. Recall 1/20/2020 is on page 11 given 60 items/page.
##pagenum = "&page="
# [NO LONGER NECESSARY] Create list of page numbers (since 1/20/2020 in on page 11 given 60 items/page).
##pages = list(range(1, 12))
# Create URL with 625 results on page.
goal_url = web_address + items_per_page + "625"
# Delete obsolete objects 'web_address' and 'items_per_page'
del web_address 
del items_per_page
# Open webpage.
web_page = urllib.request.urlopen(goal_url)
# Parse webpage.
soup = BeautifulSoup(web_page.read())
# View how tags are nested in the document.
print(soup.prettify())
## STEP 1A. FINISHED.


###     1B. Isolate html element corresponding to individual speeches.

# Using chrome's 'selectorgadget' extension.
# 'div' tag with 'class' : 'views-row' selects all 625 individual remarks.
divtags = soup.find_all("div", {"class" : "views-row"})
len(divtags)
#divtags[0]
# 'div' tag with 'class : 'views-row-1 selects the most recent remark only. Can replace '1' with any i in 1:625.
divtags_ind = soup.find_all("div", {"class" : "views-row-1"})
del divtags_ind
## STEP 1B FINISHED.


###     1C. Isolate only Biden speeches, skip other authors.

# Find out where the speech author is displayed (under 'related' on page)
## Isolates area under 'related'.
divtags[0].find_all("a")
# Isolates speech author.
divtags[0].find_all("a")[1].text
# Use for-loop to find all speeches by authors other than Biden.
authors = []
for i in range(0, len(divtags)):
    authors.append(f'{i}. {divtags[i].find_all("a")[1].text}\n')
# Search for authors that aren't joe biden.
for i in authors:
    if "Biden" not in i:
        print(i)
    else:
        pass
## 186. U.S. Congress - Zelensky speech
## 380. George W. Bush - Sept. 11 anniversary.
## 623. Donald J. Trump - 6/20/2020 remark.
## 624. Donald J. Trump - 6/20/2020 remark.
del authors
del i
# Keep only Biden speeches.
divtags2 = []
for i in divtags:
    if "Biden" in i.find_all("a")[1].text:
        divtags2.append(i)
    else:
        pass
del divtags
## STEP 2C FINISHED.



#%%
## STEP 2: Get Information.

###     2A. Define framework that accumulates info.

# Make general outline for CSV creation.
# Preliminaries.
from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import os
import random
import time
# Actual csv input.
with open("HW02_Answers.csv", "w", newline='') as f:
    w = csv.DictWriter(f, fieldnames = ("date", "title", "text", "citation"))
    w.writeheader()
    # Create correct URL with 625 speeches.
    web_address = "https://www.presidency.ucsb.edu/documents/app-categories/presidential/spoken-addresses-and-remarks"
    items_per_page = "?items_per_page="
    goal_url = web_address + items_per_page + "625"
    del web_address
    del items_per_page
    # open and parse website.
    web_page = urllib.request.urlopen(goal_url)
    del goal_url
    soup = BeautifulSoup(web_page.read())
    del web_page
    # Isolate individual remarks.
    divtags = soup.find_all("div", {"class" : "views-row"})
    del soup
    # Isolate only speeches with Biden as author.
    all_remarks = []
    for i in divtags:
        if "Biden" in i.find_all("a")[1].text:
            all_remarks.append(i)
        else:
            pass
    del divtags
    # Create counter.
    counter = 0
    # Create initial (pre-extension) part of URL.
    pre_URL = "https://www.presidency.ucsb.edu"
    
##### TEST: first 10 speeches.
    test_remarks = []
    for i in range(0, 10):
        test_remarks.append(all_remarks[i])
    del i

##### Generate for-loop for finding data.
    for i in test_remarks:
        # Update counter.
        counter += 1
######### Print update using counter.
        print("Working on " + str(counter) + " of " + str(len(test_remarks)))
        # Create empty dictionary to fill in.
        remark = {}
        # Find extension to remarks personal page.
        extension = i.find_all("div", {"class" : "field-title"})[0].find_all("a")[0]["href"]
        
###     2B. Collect 'Date of Spoken Address' information.
        remark["date"] = i.find("span", {"class" : "date-display-single"}).text
    
###     2C. Collect 'Title' information.
        remark["title"] = i.find("div", {"class" : "field-title"}).text[1:]

###     2D. Access actual remark page.
        try:
            remark_page = urllib.request.urlopen(pre_URL + extension)
        except urllib.error.URLError:
            remark["text"] = "NA"
            remark["citation"] = "NA"
            w.writerow(remark)
            continue
        remark_html = BeautifulSoup(remark_page.read())
        
###     2E. Collect 'full text of address/remarks' information.
        remark["text"] = remark_html.find_all("div", {"class" : "field-docs-content"})[0].text[1:]


###     2F. Collect 'citation/footnote' information, if it exists.
        try:
            remark["citation"] = remark_html.find_all("p", {"class" : "ucsbapp_citation"})[0].text
        except AttributeError:
            remark["citation"] = "NA"
        w.writerow(remark)
        time.sleep(random.uniform(1, 5)) # be polite, sleep!
print("ALL DONE!")

#t_extension = test_remarks[0].find_all("div", {"class" : "field-title"})[0].find_all("a")[0]["href"]
#t_remark_page = urllib.request.urlopen(pre_URL + t_extension)
#t_remark_html = BeautifulSoup(t_remark_page.read())

#t_remark_html

#remark_html.find_all("p", {"class" : "ucsbapp_citation"})[0].text


