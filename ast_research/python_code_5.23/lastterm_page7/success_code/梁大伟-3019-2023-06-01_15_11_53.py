stu={'name':'unknown','english':'unknown','python':'unknown','math':'unknown'}
a=input().split()
stu['name']=a[0]
stu['english']=eval(a[1])
stu['python']=eval(a[2])
stu['math']=eval(a[3])
stu['avg']=(eval(a[1])+eval(a[2])+eval(a[3]))/3
lst=[]
for i in range(1,4):
    lst.append(eval(a[i]))
lst.sort(reverse=True)
print(a[0],'%.2f'%(lst[0]),'%.2f'%(lst[1]),'%.2f'%(lst[2]),'%.2f'%(stu['avg']))
