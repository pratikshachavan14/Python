# 1. write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
# example myemail@google.com o/p myemail

import re
s = "myemail@google.com"
m= re.search("\w+",s,re.I)
print(m.group())

# 2. Accept lines from user and display only the lines that start with a number or any 2 alphabets
import re

lst1 = [i for i in input("Enter a list: ").split(" ")]
for i in range(len(lst1)):
    m = re.search("^\w{2}",lst1[i],re.I)
    if m!= None:
        print(lst1[i])
    else:
        pass

# 3. Write a python program to accept mobile number and validate it. it should contain exactly 10 digits.
import re
n = input("Enter a mobile number: ")
m = re.search("[0-9]{10}",n)
if m!=None:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

# 4. Write a python program to accept user name and password and validate it. username
# should contain only alphabets or digits and password length should be 8, starts with
# alphabet and should contain at least one special character(#,@) .
# accept username and password from user and validate it. if it is valid then display message
# welcome to our application. otherwise ask to re-enter.
# (allows maximum 3 attempts to accept password

import re

def validName(uname):
    return bool(re.match("[a-zA-Z0-9]+$",uname))

def validPassword(psw):
    return bool(re.match("[a-zA-Z][a-zA-Z0-9#@]{7}$",psw))

attempt = 3
while attempt > 0:
    uname = input("Enter Name: ")
    psw = input("Enter Password: ")

    if validName(uname) and validPassword(psw):
        print("Valid Credentials")
        break
    else:
        print("Invalid Credentials. Enter again.")
        attempt = attempt-1

    if attempt == 0:
        print("You have exceeded the limit to enter credentials!")
