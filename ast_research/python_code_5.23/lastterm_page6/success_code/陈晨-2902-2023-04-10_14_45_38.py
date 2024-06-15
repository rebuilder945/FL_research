k1=2
k2=1
m=eval(input())
n=1
k=0
jieguo=2
while n!=m:
    k1=k1+k2
    k2=k1-k2
    jieguo+=k1/k2
    n+=1
print("%.4f"%(jieguo))
