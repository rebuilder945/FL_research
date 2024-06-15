a=input().split()
stu={}
stu["english"]=a[1]
stu["python"]=a[2]
stu["math"]=a[3]
avg=(int(a[3])+int(a[1])+int(a[2]))/3
s=sorted(stu.items(),key=lambda x:x[1])
s=dict(s)
c=[]
for i in s:
    b=s[i]
    c.append(int(b))
print("%s %.2f %.2f %.2f %.2f"%(a[0],int(c[0]),int(c[1]),int(c[2]),avg))



