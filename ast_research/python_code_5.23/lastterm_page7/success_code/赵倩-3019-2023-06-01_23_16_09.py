a=input().split()
stu={}

stu["english"]=int(a[1])
stu["python"]=int(a[2])
stu["math"]=int(a[3])
b=(int(a[1])+int(a[2])+int(a[3]))/3

l=[]
for x in stu:
    l.append(stu[x])
l.sort()
n=l[0]
m=l[1]
d=l[2]
print(a[0],"%.2f,%.2f,%.2f"%(n,m,d),"%.2f"%b)

       



                    




