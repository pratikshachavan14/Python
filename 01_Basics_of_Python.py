################################ Basics of Python ####################################

print("Hello World!!")
a=23
b=5
if a>10:
    print("a is greater than 10")
    print("a is big number")
    if b>2:
        print("b is greater")
    else:
        print("b is smaller")
else:
    print("in else")
    print("a is small number")
print("outside if")

################################### IF DEMO #################################

#accept a number from user,
#if<10 then add 200 in the number
#if >=10 but < 30 then add 300 in th number
#if it is >= 30  and < 50 then add 400 into the number
#otherwise add 600 in the number and show the o/p

a=int(input("enetr number"))
if a<10:
    a=a+200
elif a<30:
    a=a+300
elif a<50:
    a=a+400
else:
    a=a+600
print(a)

############################### Operators #####################################

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

############################### Print Demo #####################################

a=12
b=23
c=34
print("A:",a,"B:",b,"C:",c)
print("A:"+str(a)+"B:"+str(b)+"C:"+str(c))
print(f"A: {a} B: {b} C: {c}")
print("A: {2} B: {1} C: {0}".format(a,b,c))
print("A: %d B: %d C: %d" % (a,b,c))
print(a,b,c,sep=":",end=" ")
print("welcome")
print("Hello")
print(3*2)
print("*"*80)
#a=2
if (a:=2)>2:
    print("a is greater")
else:
    print("a is smaller")