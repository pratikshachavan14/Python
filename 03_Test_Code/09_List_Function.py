# Do the following using Regular Expression:
# 1. accept lines from user and store in a list.
# convert list into dictionary as follows
# {
# “found”:[“this is algorithm”, “this is mid”],
# “not found:[“this is data”,”this is min”]
# }
# store all lines ending with m or mid in a list and assign list to key “found” in dictionary
# otherwise store it in a list and assign it to key not found”

import re

lines = []
while True:
    line = input("Enter a line (type exit to stop): ")
    if line.lower() == 'exit':
        break
    else:
        lines.append(line)

resultD = {"Found":[], "Not Found":[]}

for line in lines:
    if re.search('m$',line) or re.search('mid$',line):
        resultD['Found'].append(line)
    else:
        resultD['Not Found'].append(line)

for k,v in resultD.items():
    print(f"{k} -> {v}")

# accept strings in following format from user and store it in a list:
# 12,queen,2018,kangana,1234562018,pune
# 15,dangal,2018,aamir,34562562018,mumbai
# 12,sholay,1995,amitabh,7869272018,pune
# ---- Display movie name and year separated by, if the movie was released in 2018.
# ---- Display movies released in pune city.

import re

print("Format: Rating, Movie Name, Year, Actor/Actress, Mobile Number, City")
strlst=[]
a1=[]
a2=[]
while True:
    str1 = input("Enter a string in above format (type exit to stop): ")
    if str1.lower() == 'exit':
        break
    else:
        strlst.append(str1)

print(strlst)
for i in strlst:
    if re.search('\D2018',i) != None:       #\D: Anything but digit.
        a1.append(i.split(',')[1])
        #print(f"Movies released in 2018: {i.split(',')[1]}, {i.split(',')[2]}")

    if re.search('pune$',i) != None:
        a2.append(i.split(',')[1])
        # print(f"Movies released in Pune: {i.split(',')[1]}")

print("Movies released in 2018:",a1)
print("Movies released in Pune:",a2)

# Accept 2 patterns from user
# Accept multiple strings from user till user enters end, if string has pattern 1 then store it in list1
# If it has pattern 2 then store it in list 2 else display message pattern not found

import re

print("Format: Rating, Movie Name, Year, Actor/Actress, Mobile Number, City")
strlst=[]
lst1=[]
lst2=[]

while True:
    str1 = input("Enter a string in above format (type end to stop): ")
    if str1.lower() == 'end':
        break
    else:
        strlst.append(str1)

for i in strlst:
    if re.search('\D2018',i) != None:      
        lst1.append(i.split(',')[1])
    if re.search('pune$',i) != None:       
        lst2.append(i.split(',')[1])

print("Pattern 1: Movies released in 2018:",lst1)
print("Pattern 2: Movies released in Pune",lst2)