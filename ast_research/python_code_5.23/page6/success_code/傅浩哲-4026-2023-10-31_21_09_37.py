z=[]
m=[1,2]
n=eval(input())
a=2
b=3
z.append(a)
z.append(b)
s=0
for i in range(0,n-2):
    z.append(z[i]+z[i+1])
for j in range(0,n-2):
    m.append(m[j]+m[j+1])
for k in range(0,n):
    s+=z[k]/m[k]
print('%.4f'%s)
