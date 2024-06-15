stu={}
a=input().split()
stu["name"]=a[0]
stu["english"]=a[1]
stu["python"]=a[2]
stu["math"]=a[3]
avg=(int(a[3])+int(a[1])+int(a[2]))/3
lst=[]
lst.append(eval(a[1]))
lst.append(eval(a[2]))
lst.append(eval(a[3]))
lst.sort(reverse=True)

print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(a[0],lst[0],lst[1],lst[2],avg))
