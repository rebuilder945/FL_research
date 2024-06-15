a=input()
b=[]
for i in range(len(a)):
    b.append(a[i])
for i in range(len(b)):
    b[i]=int(b[i])
for i in range(len(b)):
    b[i]=(b[i]+5)%10
c=len(b)//2
for i in range(c):
    b[i],b[-(i+1)]=b[-(i+1)],b[i]
m=0
for i in range(len(b)):
    m=m+b[i]*10**(len(b)-1-i)
print(m)
