# -*- coding: utf-8 -*-
"""
Created on Wed May 24 20:32:50 2023

@author: anilk
"""

import pandas as pd
s1=pd.read_excel("student.xlsx")
s2=pd.read_excel("student2.xlsx",header=None)
#assign same names to the column
s2.columns=s1.columns
rating=pd.read_excel("interviewer_rating.xlsx")
#rating.drop("rating",axis=0)
rating=rating.iloc[:,1:]
students=pd.concat([s1,s2],ignore_index=True)


#what is average rating of each student
g=rating.groupby('studentid')
for sid,data in g:
    print("Student id : ",sid)
    print(data)
    print("*"*60)

rdata=g['rating'].mean()
print(rdata)
df1=pd.DataFrame(rdata)
mergedata=pd.merge(students,df1,left_on='stuid',right_on='studentid')

#if the marks of students >80 and rating > 4 then 
#allocate Python project 
#if rating > 3 and marks > 90 then assign java project
#if rating>4  then assign python training
#otherwise assign java training
def myfunction(information):
    print("details",information)
    if information[0]>80 and information[1]>4:
        return 'Python Project'
    elif information[0]>90 and information[1]>3:
        return 'Java Project'
    elif information[1]>4:
        return 'Python Training'
    else:
        return 'Java Training'
    
mergedata['technology']=mergedata[['marks','rating']].apply(myfunction,axis=1)



#if student marks > 80 then location is pune:
#    <80 and > 70 then location is delhi
#    otherwise mumbai
def assignlocation(mks):
    if mks>80:
        return 'Pune'
    elif mks>=70:
        return 'Delhi'
    else:
        return 'Mumbai'
mergedata['location']=mergedata['marks'].apply(assignlocation)



#display  pie chart for how many students are 
#allocated to mumbai, pune location and delhi location
import matplotlib.pyplot as plt
result=mergedata['location'].value_counts()
print(result)
plt.pie(result.values,labels=result.index,colors=['c','b','g'],startangle=90,explode=(0,0,0.1))
plt.show()

#minimum, max average, marks for each technology
mergedata['techname']=mergedata['technology'].map(lambda x:x.split(" ")[0])





 
