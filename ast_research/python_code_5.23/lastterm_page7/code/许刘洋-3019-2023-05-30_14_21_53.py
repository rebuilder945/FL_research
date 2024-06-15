stu={}
a=list(input().split(' '))
b=a[1:4]
c=list(map(eval,b))
stu['name']=a[0]
stu['english']=a[1]
stu['python']=a[2]
stu['math']=a[3]
stu['avg']=(sum(c))/3
c.sort(reverse=True)
print(stu['name'],'%.2f %.2f %.2f %.2f'%(c[0],c[1],c[2],(sum(c))/3
