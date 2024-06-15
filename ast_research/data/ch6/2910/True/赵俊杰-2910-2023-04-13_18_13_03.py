h=eval(input())
N=eval(input())
s=h
N=N-1
while N>0:
    s=s+h
    N=N-1
    h=h/2
print("%.2f"%(s))

