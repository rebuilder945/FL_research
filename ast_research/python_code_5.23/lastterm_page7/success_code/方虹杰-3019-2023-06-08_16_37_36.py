stu={}
a=input().split()
stu["name"]=a[0]
stu["english"]=a[1]
stu["python"]=a[2]
stu["math"]=a[3]
b=list(map(int,a[1:]))
b.sort(reverse=True)
c=sum(b)/len(b)
print(a[0],"%.2f %.2f %.2f %.2f"%(b[0],b[1],b[2],c))
