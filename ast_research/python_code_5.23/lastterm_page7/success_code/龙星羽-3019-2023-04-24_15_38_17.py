a=input().split()
stu={}
stu["name"]=a[0]
a1=stu["english"]=eval(a[1])
a2=stu["python"]=eval(a[2])
a3=stu["math"]=eval(a[3])
si=[a1,a2,a3]
avg=sum(si)/3
l=max(si)
s=min(si)
b=sum(si)-l-s
print('%s %.2f %.2f %.2f %.2f'%(a[0],l,b,s,avg))
