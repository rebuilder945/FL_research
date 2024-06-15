a=input().split()
stu={}
stu["name"]=a[0]
a1=stu["english"]=eval(a[1])
a2=stu["python"]=eval(a[2])
a3=stu["math"]=eval(a[3])
avg=int(a1+a2+a3)/3
stu.sort(key=lambda x:stu[1])
print("%.2f"%stu[1])
