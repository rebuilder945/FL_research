a=input()
b=[]
for i in a:
    n=(int(i)+5)%10
    b.append(str(n))
for i in range(len(b)-1):
    b[i],b[-1-i]=b[-1-i],b[i]
c=b[0]+b[1]+b[2]
d=int(c)
print(d)
