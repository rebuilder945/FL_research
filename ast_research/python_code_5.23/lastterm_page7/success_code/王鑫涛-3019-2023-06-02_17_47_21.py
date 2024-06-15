a=input().split()
stu={}
stu['name']=a[0]
stu['english']=eval(a[1])
stu['python']=eval(a[2])
stu['math']=eval(a[3])
stu['avg']=(eval(a[1])+eval(a[2])+eval(a[3]))/3
b=a[1:]
b.sort()
print(stu['name'],end='')
for i in b:
    for r in stu:
        if stu[r]==eval(i):
            print('%.2f'%stu[r],end='')
print('%.2f'%stu['avg'])
