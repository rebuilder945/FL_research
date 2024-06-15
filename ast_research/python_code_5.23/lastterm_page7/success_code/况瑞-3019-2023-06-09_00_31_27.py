stu={}
a=input().split()
stu['name']=a[0]
stu['english']=eval(a[1])
stu['python']=eval(a[2])
stu['math']=eval(a[3])
b=(eval(a[1])+eval(a[2])+eval(a[3]))/3
ls=list(stu.values())
ls.remove(ls[0])
ls.sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(stu['name'],ls[0],ls[1],ls[2],b))

