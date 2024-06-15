stu={}
a=list(input().split(' '))
b=a[1:]
c=list(map(eval,b))
stu['avg']=((sum(c))/3)
c.sort(reverse=True)
print(a[0],'%.2f %.2f %.2f %.2f'%(c[0],c[1],c[2],(sum(c))/3))
