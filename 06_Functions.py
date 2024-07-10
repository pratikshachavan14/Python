def f1(a,b,c):
    print(a,b,c)

f1(1,2,3)

def f2(a,b=20,c=30):
    print(a,b,c)
    
f2(10)
f2(12,25)
f2(12,13,14)
f2(b=12,c=13,a=14)

'''
def f3(a=10,b,c=30):
    print(a,b,c)
f3(1,2,3)
'''

def addition(a,b):
    return a+b

num=int(input("enetr number1"))
num2=int(input("enter number2"))
print("addition ",addition(num,num2))


############################## MATCH CASE ######################################

num=10
match num:
    case 10:
        print("num is 10")
    case 20:
        print("num is 20")
    case others:  # this is default case
        print("num is other than 10 and 20")

color="yellow"
match color:
    case "Red"|"yellow":  #this is for multiple values
        print("color is either red or yellow")
    case "green":
        print("the color is green")
    case _:  #this is default case
        print("The color is blue")
        