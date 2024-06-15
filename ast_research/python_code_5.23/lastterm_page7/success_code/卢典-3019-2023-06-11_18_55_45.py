stu={}
a=input().split(' ')
stu['name']=a[0]
stu['english']=a[1]
stu['python']=a[2]
stu['math']=a[3]
lis1=list(stu.values())
b=stu['name']
lis1.remove(b)
lis1=list(int(i) for i in lis1)
lis1.sort(reverse=True)
stu['ave']='%.2f'%(sum(lis1)/len(lis1))
print(stu['name'],end=' ')
for x in lis1:
    print("%.2f"%x,end=' ')
print(stu['ave'])
