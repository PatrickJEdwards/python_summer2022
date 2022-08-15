import re
import os
# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()
os.chdir('C:\\Users\\edwar\\Documents\\GitHub\\python_summer2022\\Day5\\Lab')

## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

# Designate pattern to search for.
## 're.I' tells python to ignore the case (The vs. the).
keyword = re.compile(r" the " or r"The ")

# Lines containing 'the'
lines = []
for i, line in enumerate(obama):
    if  keyword.search(line):
        print(i)
        print(line)
        lines.append(i)

# Lines NOT CONTAINING 'THE'
not_lines = []
for i, line in enumerate(obama):
    if not keyword.search(line):
        print(i)
        print(line)
        not_lines.append(i)
        
print(lines)
print(not_lines)
len(not_lines)



# TODO: print lines that contain a word of any length starting with s and ending with e
pattern = re.compile(r'\bs\S+e\b')

lines2 = []
for i, line in enumerate(obama):
    if  pattern.search(line):
        print(i)
        print(line)
        lines2.append(i)


## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = 'Please enter a date in the following format: 08.18.21'

datepattern = re.compile(r'(\d*)\.(\d*)\.(\d*)')
datesearch = datepattern.search(date)
print(f"Month: {datesearch.group(1)}\nDay: {datesearch.group(2)}\nYear: {datesearch.group(3)}")





