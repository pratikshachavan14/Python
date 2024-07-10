############################## BitWise Demo ######################################

a=11
b=9
print("a",bin(a))
print("b",bin(b))
d=b<<4   #010010000
result=d|a
print(result,"--->",bin(result))
#to separate them
print("mask",int(0b01111))
a1=result&15
print(a1)
b1=result>>4
print(b1)

############################## FOR LOOP ######################################

#for loop demo
#if you know the number of iterations in advance
#to print numbers 1 to 10
for i in range(1,11): #1-10
    print(i,end=" ")
print()
print("end of loop")
for i in range(10): #0-9
    print(i,end=" ")
print()
print("end of loop")

for i in range(3,21,3): #0-9
    print(i,end=" ")
print()
print("end of loop")

############################## MENU DRIVEN ######################################

import sys
#calculate factorial of a number
def factorial(num):
    fact=1
    for i in range(2,num+1):
        fact=fact*i
    return fact

#to check whether given number is prime or not
def checkprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

#display the table of the given number"
def printtable(num):
    for i in range(1,11):
        print(f"{num} * {i}= {num*i}")


choice=0
while choice!=4:
    choice=int(input("""
    1. factorial
    2. prime number
    3. Table of a number
    4. exit
    choice:"""))
    match choice:
        case 1:
            print("factorial selected")
            num=int(input("enetr number"))
            answer=factorial(num)
            print("Factorial :",answer)
        case 2:
            print("prime number selected")
            num=int(input("enetr number"))
            answer=checkprime(num)
            print("The number is prime" if answer else "The number is not prime")
        case 3:
            print("print table selectd")
            num=int(input("enetr number"))
            printtable(num)
        case 4:
            #sys.exit(0)
            print("Thank you for visiting.....")
        case others:
            print("it is default case")

############################## OPERATORS ######################################

#to find maximum of 3 numbers
a=int(input("enter number"))  #always accepts and store data in the form of strings
b=int(input("enetr number2"))
c=int(input("enter number 3"))
if a>b and a>c:
    print("a is the maixmum value",a)
else:
    if b>a and b>c:
        print("b is the maixmum value",b)
    else:
        print("c is the maximum value",c)

if a>b and a>c:
    print("a is the maixmum value",a)
elif b>a and b>c:
    print("b is the maixmum value",b)
else:
    print("c is the maximum value",c)
    
print("addition:",a+b,a,b,sep=":")
print("addition : ",end="--->")
print(a+b)
print("welcome")


a=23
b=35
m=a if a>b else b

############################## PRIME NUMBERS ######################################

#to chek the number is prime or not
num=int(input("enter a number"))
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break
if flag:
    print("the number is not prime")
else:
    print("the number is prime")

#9
    #5
for i in range(2,num):
    if num%i==0:
        print("The number is not prime")
        break
else: #if break statement does not get executed
    print("The number is prime")

############################## Monthly Calender ######################################

#accept number of days in a month, 29,28,30,31
#when the month starts (mon-0,tue-1)
while True:
    numdays=int(input("enter days"))
    if numdays>=28 and numdays<=31:
        break
while True:
    startday=int(input("enetr start day 0-mon 1-tuesday .....6-sunday"))
    if startday>=0 and startday<=6:
        break
print("Mon\tTue\tWed\tThu\tFri\tsat\tsun")
#it will print spaces before 1, useful only for line 1
print("   \t"*startday,end="")
count=startday
for i in range(1,numdays+1):
    print(" "+str(i),end="\t")
    count=count+1
    #to bring the cursor on the next line
    if count==7:
        print()
        count=0

############################### WHILE LOOP #####################################

#accept number of days in a month, 29,28,30,31
#when the month starts (mon-0,tue-1)
while True:
    numdays=int(input("enter days"))
    if numdays>=28 and numdays<=31:
        break
while True:
    startday=int(input("enetr start day 0-mon 1-tuesday .....6-sunday"))
    if startday>=0 and startday<=6:
        break
print("Mon\tTue\tWed\tThu\tFri\tsat\tsun")
#it will print spaces before 1, useful only for line 1
print("   \t"*startday,end="")
count=startday
for i in range(1,numdays+1):
    print(" "+str(i),end="\t")
    count=count+1
    #to bring the cursor on the next line
    if count==7:
        print()
        count=0
