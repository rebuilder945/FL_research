z=[]
m=[]
j=[]
n=eval(input())
a=2
b=3
z.append(a)
z.append(b)
for i in range(0,n-2):
    z.append(z[i]+z[i+1])
print(z)
