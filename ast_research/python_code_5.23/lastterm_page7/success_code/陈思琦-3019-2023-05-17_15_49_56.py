from audioop import reverse


a=list((input().split()))
stu={}
c=[]
stu['english']=round(int(a[1]),2)
stu['python']=round(int(a[2]),2)
stu['math']=round(int(a[3]),2)
newstu=dict(sorted(stu.items(),key=lambda x:x[1],reverse=True))
for key in newstu.keys():
    c.append(key)
b=(stu['math']+stu['python']+stu['english'])/3
stu['avg']=b
stu['name']=a[0]
print('%s %.2f %.2f %.2f %.2f '%(stu['name'],newstu[c[0]],newstu[c[1]],newstu[c[2]],stu['avg']))

