h=float(input())
N=eval(input())
num=[h]
i=1
while i<N:
    i=i+1
    num.append(h)
    h=h/2
s=sum(num)
print("%.2f"%s)
