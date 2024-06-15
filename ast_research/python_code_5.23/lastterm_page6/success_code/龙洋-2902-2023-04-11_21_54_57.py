n=eval(input())
lis=[1,2]
p=0
for x in range(n-1):
    q=lis[-1]+lis[-2]
    lis.append(q)
for x in range(n):
    p=p+lis[x+1]/lis[x]
print("%.4f"%p)
    
