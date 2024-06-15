a=eval(input())
d=[]
for y in range(a):
    if str(y)[0]==str(y)[-1]:
        d.append(y)
b=[]
for i in d:
    c=True
    for x in range(2,i):
        if i%x==0:
            c=False
            break
    if c:
        if i!=0 and i!=1:
            b.append(i)
for m in range(len(b)):
    print(b[m],end='')


