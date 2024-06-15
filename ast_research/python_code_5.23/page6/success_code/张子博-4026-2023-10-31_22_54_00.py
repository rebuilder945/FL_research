n=eval(input())
m=2
z=1
u=3
b=[]
for i in range(n):
        d=float(m/z)
        b.append(d)
        u=z
        z=m
        m=m+u
k=sum(b)
print('%.4f'%k)




