h=int(input())
n=int(input())
b=[2*h]
for i in range(3,n+1):
    x=h*0.5
    b.append(x)
c=sum(b)
print("%.2f" %c)


