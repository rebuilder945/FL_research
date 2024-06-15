a=input().split()
for i in range(1,4):
    a[i]=int(a[i])
t=a[1:4]
t.sort(reverse=True)
print(a[0],end=' ')
for i in t:
    print('%.2f'%(i),end=' ')
print('%.2f'%(sum(t)/len(t)))
