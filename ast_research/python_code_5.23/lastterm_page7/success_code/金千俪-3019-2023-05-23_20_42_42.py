lst=input().split()
stu={}
stu["name"]=lst[0]
stu["english"]=int(lst[1])
stu["python"]=int(lst[2])
stu["math"]=int(lst[3])
del stu["name"]
stuSort  = sorted(stu.values(),reverse=True)
avge=sum(stuSort)/len(stuSort)
stuSort = ['{:.2f}'.format(i) for i in stuSort]
print(lst[0],*stuSort,"%.2f"%(avge),sep=" ")
