a=input().split()
stu={}
stu["english"]=int(a[1])
stu["python"]=int(a[2])
stu["math"]=int(a[3])
stu["name"]=a[0]
stu["avg"]=(int(a[2])+int(a[1])+int(a[3]))/3
b=[int(a[1]),int(a[2]),int(a[3])]
b=sorted(b)
print(b)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(stu["name"],b[2],b[1],b[0],stu["avg"]))
