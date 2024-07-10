lst=[] #empty list
lst=[10,20,30,1,2,3]
print("length",len(lst))
#to retrieve the value at given index position
print(lst[3])
lst1=[1,2,3,"xxxx"]
lst2=[12,13,"xxx",[100,200,300]]
#to get the value 200
print("to get the value from nested list:",lst2[3][1])
#to overwrite the value in the list
lst2[1]=100
print(lst2)

#add a value at the end
lst2.append("sssss")
lst2.append(23)
lst2.append([12,11,11])
print(lst2)

#to add multiple values in the list at the end
lst2.extend("abcd")
lst2.extend([11,12,13,22,34])
print(lst2)

# to add in between by position
lst2.insert(1,1000)
print(lst2)

##################################################################

lst2=[1,2,"aaa",[12,13,14],100,200]
# to add in a nested list
lst2[3].append(100)
print(lst2)
lst2[3].extend([1,2,3,4])
print(lst2)
lst2[3].insert(2,1000)

####################################################################

lst2=[12,13,14,11,41,12,13,14]
#to delete the values
#pop remove
#to delete the last value
value=lst2.pop()
#to delete the value at particular position
lst2.pop(4)
print("after pop",lst2)

#to delete by value,
#to delete the first occurance of 100 from the list if found
#throws exception if the number not found
lst2.remove(12)
print("after remove",lst2)


#write the code to delete all occurances of value 100
num=12
lst=[1,2,3,12,10,[12,13,14],20,12,12]

lst.remove(12)
print(lst)
while num in lst:
    lst.remove(num)

lst=[1,2,3,[11,22,33],9,10,["aa","bb","cc"]]
for d in lst:
    if isinstance(d,list):
        print("this is list")
    else:
        print("it is other than list")

####################################################################

lst=[10,20,30,[12,1,10,23],10,10,3,4,10]
#find the position of 20
print("position of 20:",lst.index(20))
#to find number of occurances of the given value
print("number of occurence of 10",lst.count(10))
lst.reverse()
print("after reverse",lst)
lst=[12,13,14,1,2,5,3,24,72]
#in the list if all the values are of same type then
#only sort is possible, it will sort in ascending order
lst.sort()
print("after sort",lst)
#only sort is possible, it will sort in descending order
lst.sort(reverse=True)
print("after reverse",lst)
#to remove all the elements from the list
#lst.clear()

####################################################################

lst=[1,2,3,4]
lst1=lst
lst.append(100)
print(lst,lst1)
lst2=lst.copy()
lst.append(200)
print(lst,lst1,lst2)

lst=[1,2,["a","b","c"],3,4]
lst1=lst.copy()
lst.append(400)
print(lst,lst1)
lst[2].append("d")
print(lst,lst1)

import copy
lst3=copy.deepcopy(lst)
lst[2].append("xxxx")
print(lst,lst3)