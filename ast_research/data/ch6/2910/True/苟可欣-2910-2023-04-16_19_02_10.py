h=eval(input())
N=eval(input())
H=h
lst=[h]
for x in range(N-1):
    H=H/2
    h1=2*H
    lst.append(h1)
s=sum(lst)
print("%.2f"%(s))
