lst=[12,13,11,24,11,23,7,16,28]
lst2=list(filter(lambda x:x%4==0 and x>15,lst))
print(lst2)

lst3=list(map(lambda x:x*x  ,lst))
print(lst3)

def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
   

lst=[3,4,2,5]
lst3=list(map(lambda x:factorial(x),lst))
print(lst3)

from functools import reduce

#find addition of all numbers
ans=reduce(lambda x,y:x+y,lst)
print(ans)

#find maximum number
ans=reduce(lambda x,y:x if x>y else y,lst)

sum(lst)
min(lst)
max(lst)

#concatenate all strings
lst=["python","perl","linux","os"]
ans=reduce(lambda x,y:x+y,lst)

#it will concatenate first 3 characters of all strings
ans=reduce(lambda x,y:x+y[:3],lst,"")
print(ans)

#find a string with maximum length

#find the string which is the last one after sorting it in reverse order
#without using sort function












