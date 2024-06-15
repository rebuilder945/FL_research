n=eval(input())
s1=2
s=0
for i in range(n):
    s+=s1
    s1=1+1/s1
print("%.4f"%(s))

