ls=input().split()
stu={}
a=ls[0]
b=int(ls[1])
c=int(ls[2])
d=int(ls[3])
stu['english']=b
stu['python']=c
stu['math']=d
ls2=sorted(stu.items(),key=lambda x:x[1],reverse=True)
f=ls2[0][1]
g=ls2[1][1]
h=ls2[2][1]
stu['name']=a
sum=d+b+c
avg=sum/3
stu['avg']=avg
print(stu['name'],"%.2f %.2f %.2f %.2f"%(f,g,h,stu['avg']))

