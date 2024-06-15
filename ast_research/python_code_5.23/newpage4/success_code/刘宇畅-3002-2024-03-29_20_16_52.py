a=eval(input())
b=len(a)
c=sum(a)
d=b/c
e=d-int(d)
if e==0:
    print(int(d))
elif e!=0:
    print('%.2f'%(d))
