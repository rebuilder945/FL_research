stu={"name":"Zhang","english":80,"python":90,"math":100}
a=input().split()
stu['name']=a[0]
stu['english']=(a[1])
stu['python']=(a[2])
stu['math']=(a[3])
avg=(float(a[1])+float(a[2])+float(a[3]))/3
lst=[]
for i in range(3):
    lst.append(float(a[i+1]))
lst.sort()
lst.reverse()
print('%s %.2f %.2f %.2f %.2f'%(a[0],lst[0],lst[1],lst[2],avg))


