a=input()
b=[]
c=str()
for i in a:
    n=int((int(i)+5)%10)
    b.append(str(n))
for i in range(0,len(b)):
    b[i],b[-1-i]=b[-1-i],b[i]
for n in b:
    c=n+c
print(c)
