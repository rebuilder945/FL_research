a=eval(input())
b=[]
c=0
for i in str(a):
    b.append(i)
d=len(b)
for x in b:
    c+=int(i)**d
    d-=1
if c==a:
    print("%d"%(a))
else:
    print('None')

