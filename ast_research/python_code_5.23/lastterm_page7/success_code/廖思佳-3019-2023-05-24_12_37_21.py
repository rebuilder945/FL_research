n=input()
a,b,c,d=n.split()
stu={}
stu["name"]=a
stu["english"]=int(b)
stu["pyhton"]=int(c)
stu["math"]=int(d)
sName=stu.pop("name")
list1=sorted(list(stu.values()),reverse=True)
avg=sum(list1)/3
print("%s %.2f %.2f %.2f %.2f"%(sName,list1[0],list1[1],list1[2],avg))

