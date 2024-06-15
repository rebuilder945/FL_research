h=eval(input())
N=eval(input())
H=h
lst=[h]
for x in range(N-1):
    H=H/2
    lst.append(H)
s=sum(lst)
print("%.2f"%(s))
