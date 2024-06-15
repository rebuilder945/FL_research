n,e,p,m=input().split()
stu={}
stu["name"]=n
stu["english"]=e
stu["python"]=p
stu["math"]=m
stu["avg"]=(eval(e)+eval(p)+eval(m))/3
sutlist=[]
for k,v in stu.items():
    if k!='name' and k!= 'avg':
        sutlist.append([k,v])
print(sutlist)
sutlist.sort(key=lambda x:x[1])
print(stu["name"],end=" ")
for i in sutlist:
    print("%.2f" %eval(i[1]),end=" ")
print("%.2f" %stu["avg"])
