a=input().split()
print(a[0],end=" ")
b=a.copy()
del b[0]
b.sort(reverse=True)
avg=sum(b)/3
stu={}
stu["name"]=a[0]
stu["english"]=int(a[1])
stu["python"]=int(a[2])
stu["math"]=int(a[3])
stu["avg"]=avg
for x in b:
    print('%.2f'%(x),end=" ")
print('%.2f'%b)

