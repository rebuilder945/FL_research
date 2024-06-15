a=input().split()
stu={}
stu['name']=a[0]
stu['english']=a[1]
stu['python']=a[2]
stu['math']=a[3]
stu['avg']=str((eval(a[1])+eval(a[2])+eval(a[3]))/3)
b=a[1:]
b.sort()
print(stu['name'],end='')
for i in b:
    for r in stu:
        if stu[r]==i:
            print('%.2f'%stu[r],end='')
print('%.2f'%stu['avg'])
