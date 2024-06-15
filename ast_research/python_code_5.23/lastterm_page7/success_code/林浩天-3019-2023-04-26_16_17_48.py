a,b,c,d=input().split()
stu={}
stu['name']=a
stu['english']=int(b)
stu['python']=int(c)
stu['math']=int(d)
stu['avg']=(stu['english']+stu['python']+stu['math'])/3
e=stu['avg']
m=["%.2f"%float(d),"%.2f"%float(b),"%.2f"%float(c)]
y=[int(i) for i in m]
print(y)
x=sorted(m,reverse=True)
print(a,end=" ")
for i in x:
    print(i,end=" ")
print("%.2f"%e)

