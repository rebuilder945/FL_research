n=eval(input())
m=2
z=1
u=3
b=[]
for i in range(n):
    if i<3:
        d=float(m/z)
        b.append(d)
        z=m
        m=i+1+m
    else:
        d=float(m/z)
        b.append(d)
        z=m
        m=m+u
        u=u+i-1


k=sum(b)
print('%.4f'%k)




