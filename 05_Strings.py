s="this is cat, cat is cute, where is you cat?"
pos=s.find('cat')
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
#to find position of all occurences of the given string
search=input("enetr string to search")
pos=s.find(search)
while pos!=-1:
    print("position :",pos)
    pos=s.find(search,pos+1)

####################################################################

s="this is cat, cat is cute, where is you cat?"
pos=s.find("cat") #8
print("find position",pos)
pos1=s.index("cat") #8
print("index position",pos1)
pos=s.find("dog")#-1
print("find position dog",pos)
pos1=s.index("dog")  #exception
print("index position dog",pos1)

####################################################################

s="aaaasssaaddssThis is stringsssaaaeee"
print(s.strip("asde"))
s="aaaasssaaddssThis is stringsssaaaeee"
print(s.rstrip("asde"))
s="aaaasssaaddssThis is stringsssaaaeee"
print(s.lstrip("asde"))

acno="XXXX1234XXXX"
print(acno.strip("X"))

####################################################################

s="this is cat, the cate is cute, where is you cat?"
print(s.replace("cat","dog",1))

s="this is cat, cat is cute, where is you cat?"
pos=s.find('cat')
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
pos=s.find('cat',pos+1)
print("position :",pos)
print("*"*60)
pos=s.rfind('cat')
print("position :",pos)
pos=s.rfind('cat')
print("position :",0,pos-1)

####################################################################

#to find position of all occurences of the given string
search=input("enetr string to search")
pos=s.find(search)
while pos!=-1:
    print("position :",pos)
    pos=s.find(search,pos+1)

s="this is cat, cat is cute, where is you cat?"
pos=s.find("cat") #8
print("find position",pos)
pos1=s.index("cat") #8
print("index position",pos1)
pos=s.find("dog")#-1
print("find position dog",pos)
#pos1=s.index("dog")  #exception
#print("index position dog",pos1)
a=5
for j in range(5):
    a=a+2
    if a<7:
         print("smaller",a)
         break
else:
    print("bigger",a)