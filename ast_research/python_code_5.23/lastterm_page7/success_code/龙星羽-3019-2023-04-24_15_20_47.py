from posixpath import split


a=input().split()
stu={}
stu["name"]=a[0]
a1=stu["english"]=eval(a[1])
a2=stu["python"]=eval(a[2])
a3=stu["math"]=eval(a[3])
avg=(a1+a2+a3)/3
a.sort(reverse=True)
print('%s,%.2f,%.2f,%.2f,%.2f'%(a[0],a1,a2,a3,avg),end=' ')
