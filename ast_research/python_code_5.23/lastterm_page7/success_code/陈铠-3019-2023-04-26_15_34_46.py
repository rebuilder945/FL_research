lst=input().split(' ')
sb=lst[1:4]
num=[int(x) for x in sb]
num.sort()
num.reverse()
a=(int(num[0])+int(num[1])+int(num[2]))/3
b=int(num[0])
c=int(num[1])
d=int(num[2])
print(lst[0],'%.2f'%(b),'%.2f'%(c),'%.2f'%(d),'%.2f'%(a))
