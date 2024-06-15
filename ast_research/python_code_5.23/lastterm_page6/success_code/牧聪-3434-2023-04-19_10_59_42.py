h=int(input())
a=h
n=int(input())
length=[]
for x in range(n):
    h="%.2f"%h/2
    length.append(h)
b=sum(length)
print("%.2f"%(2*b+a-h))
