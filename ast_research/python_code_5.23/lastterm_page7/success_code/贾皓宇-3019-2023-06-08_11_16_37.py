a=list(input().split())
a[1]=int(a[1])
a[2]=int(a[2])
a[3]=int(a[3])
lst=[a[1],a[2],a[3]].sort()
avg=sum(lst)/3
print('%s %.2f %.2f %.2f %.2f'%(a[0],lst[0],lst[1],lst[2],avg))
