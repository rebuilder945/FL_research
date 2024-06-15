h=eval(input())
N=eval(input())
s=h
if N>2:
    for i in range(2,N+1):
        s+=2*(h/(2**(i-1)))
        i+=1
else:
    pass
print("%.2f"%(s))
