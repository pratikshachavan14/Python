lst=[("DAI",60),("DUASP",20)]

#add new course in the list
def addnewcourse():
    cname=input("enter course name")
    capacity=int(input("enter capacity"))
    #check the course is not duplicate
    pos,data=searchByName(cname)
    if pos!=-1:
        return False
    lst.append((cname,capacity))
    return True

#search the course by name
def searchByName(cname):
    for idx,data in enumerate(lst):  #[(0,("DAI",60)),(1,()),(2,())
        if data[0]==cname:
            return idx,data
    return -1,None

def deletebyname(cname):
    pos,data=searchByName(cname)
    if pos!=-1:
        ans=input(f"{data[0]}---->{data[1]}do you want to delete (y/n)")
        if ans=="y":
            lst.pop(pos)
            #lst.remove(data)
            return 1
        else:
            return 2
    else:
        return 3
    
def updatecapacity(cname,ncapacity):
    pos,data=searchByName(cname)
    if pos!=-1:
        ans=input(f"{data[0]} {data[1]} do you want to update")
        if ans=="y":
            #lst[pos]=(data[0],ncapacity) or
            lst[pos]=(cname,ncapacity)
            return 1
        else:
            return 2
    else:
        return 3

def updatename(oldname,ncname):
    pos,data=searchByName(oldname)
    if pos!=-1:
        ans=input(f"{data[0]} {data[1]} do you want to update name")
        if ans=="y":
            lst[pos]=(ncname,data[1])
            return 1
        else:
            return 2
    else:
        return 3

#return list of courses with capacity> given capacity
def searchByCapacity(gcapacity):
    lst1=[]
    for cn,capa in lst:
        if capa>=gcapacity:
            lst1.append((cn,capa))
    if len(lst1)>0:
        return lst1
    else:
        return None
    

#display all the courses
def displayall(mylst=lst):
    for cn,capa in mylst:
        print(f"{cn} ---> {capa}")
        
#sort data either on name or capcity
def sortdata(ch1):
    lst2=lst.copy()
    if ch1==1:
        lst2.sort()
    else:
        lst2.sort(key=lambda x:x[1])
    return lst2

choice=0
while choice!=9:
    choice=int(input("""
    1. add new course
    2. delete the course by name
    3. update capacity
    4. update coursename
    5. display courses in sorted order
    6. display course with capacity > given capacity
    7. display all
    8. display by name
    9. exit"""))
    match choice:
        case 1:
            status=addnewcourse()
            if status:
                print("new course added")
            else:
                print("duplicate course name")
        case 2:
            cname=input("enetr course name to delete")
            status=deletebyname(cname)
            if status==1:
                print("course found and deleted")
            elif status==2:
                print("course found but not deleted")
            else:
                print("course not found")
           
        case 3:
            cname=input("enetr course name to update")
            ncapacity=int(input("eneter new capacity"))
            status=updatecapacity(cname,ncapacity)
            if status==1:
                print("course found and updated")
            elif status==2:
                print("course found but not updated")
            else:
                print("course not found")
        case 4:
            oldcname=input("enetr course name to update")
            ncname=input("enetr new course name to update")
            status=updatename(oldcname,ncname)
            if status==1:
                print("course found and updated")
            elif status==2:
                print("course found but not updated")
            else:
                print("course not found")
        case 5:
            ch1=int(input("1.cname  2.capacity"))
            lst2=sortdata(ch1)
            displayall(lst2)
           
        case 6:
            capacity=int(input("enetr capacity to search"))
            lstcourses=searchByCapacity(capacity)
            if lstcourses!=None:
                displayall(lstcourses)
            else:
                print("not found")
        case 7:
            displayall()
            pass
        case 8:
            cname=input("enetr course name to search")
            pos,data=searchByName(cname)
            if pos!=-1:
                print(f"{data[0]}---->{data[1]}")
            else:
                print("not found")
        case 9:
            print("Thank you for visiting.....")
        case _:
            print("wrong choice")
        



    
