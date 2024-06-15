n=int(input())
s=1
if n==1:
    print("%.4f"%(s))
else:
    for i in range(1,n+1):
        s+=2-1/i
    print("%.4f"%(s))


