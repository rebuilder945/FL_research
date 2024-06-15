a=list(input().split())
stu={}
stu['name']=a[0]
stu['english']=int(a[1])
stu['python']=int(a[2])
stu['math']=int(a[3])
avg=(int(a[1])+int(a[2])+int(a[3]))/3
print(stu['name'],end=" ")
b=[]
b.append(int(a[1]))
b.append(int(a[2]))
b.append(int(a[3]))
b.sort(reverse=True)
print("%.2f"%int(b[0]),end=" ")
print("%.2f"%int(b[1]),end=" ")
print("%.2f"%int(b[2]),end=" ")
print("%.2f"%avg,end=" ")
