a,b,c,d=input().split()
b=float(b)
c=float(c)
d=float(d)
stu={}
stu['name']=a
stu['english']=b
stu['python']=c
stu['math']=d
ls=[]
for k in stu:
    ls.append(stu[k])
ls.pop(0)
ls.sort(reverse=True)
stu['avg']=sum(ls)/len(ls)
a=ls[0]
b=ls[1]
c=ls[2]
print('{} {:.2f} {:.2f} {:.2f} {:.2f}'.format(stu['name'],a,b,c,stu['avg']))
