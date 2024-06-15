h=float(input())
N=int(input())
b=[h]
b.append(h)
for x in range(3,N+1):
    a=((1/2)**(x-2))*h
    b.append(a)
c=sum(b)
print("%.2f"%c)
