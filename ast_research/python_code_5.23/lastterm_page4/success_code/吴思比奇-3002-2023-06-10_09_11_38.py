a=eval(input())
le=len(a)
s=sum(a)
d=s/le
if s%le==0:
    print(int(d))
else:
    print('%.2f'%d)
