a=input().split()
stu={}
stu['name']=a[0]
stu['english']=int(a[1])
stu['python']=int(a[2])
stu['math']=int(a[3])
stu['avg']=(int(a[1])+int(a[2])+int(a[3]))/3
ls=[int(a[1]),int(a[2]),int(a[3])]
ls.sort(reverse=True)
print(stu['name'],end=' ')
for i in ls:
    print('%.2f'%i,end=' ')
print('%.2f'%stu['avg'])
