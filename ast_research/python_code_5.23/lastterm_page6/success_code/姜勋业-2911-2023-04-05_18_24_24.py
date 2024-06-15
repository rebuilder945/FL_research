a=input()
b=0
for i in range(len(a)):
    k=int(a[i])
    k=(k+5)%10
    b=10**i*k+b
b=str(b)
b[0],b[-1]=b[-1],b[0]
b[1],b[-2]=b[-2],b[1]
b=int(b)
print(a)
