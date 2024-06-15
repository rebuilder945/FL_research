h=eval(input())
N=eval(input())
b=[]
for i in range(0,N+1):
    h=0.5*h
    b.append(h)
c=float(sum(b))
print("%.2f"%c)

