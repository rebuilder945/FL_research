stu={}
a,b,c,d=input().split( )
stu['name'],stu['english'],stu['python'],stu['math']=a,b,c,d
stu['avg']=(int(b)+int(c)+int(d))/3
l=[float(b),float(c),float(d)]
l.sort(reverse=True)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(stu['name'],l[0],l[1],l[2],stu['avg']))
