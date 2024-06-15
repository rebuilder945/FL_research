a=input()
b=[]
for i in a:
    n=(int(i)+5)%10
    b.append(str(n))
b[0],b[-1]=b[-1],b[0]
b[1],b[-2]=b[-2],b[1]
c=b[0]+b[1]+b[2]
d=int(c)
print(d)
