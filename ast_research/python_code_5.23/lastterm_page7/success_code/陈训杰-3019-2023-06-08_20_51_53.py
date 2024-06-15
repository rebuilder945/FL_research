n,e,p,m=input().split()
stu={}
stu["name"]=n
stu["english"]=eval(e)
stu["python"]=eval(p)
stu["math"]=eval(m)
stu["avg"]=(eval(e)+eval(p)+eval(m))/3
sutlist=[]
for k,v in stu.items():
    if k!='name' and k!= 'avg':
        sutlist.append([k,v])
sutlist.sort(key=lambda x:x[1],reverse=True)
print(stu["name"],end=" ")
for i in sutlist:
    print("%.2f" %i[1],end=" ")
print("%.2f" %stu["avg"])
