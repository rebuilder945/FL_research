def issu(n): 
    j=0
    for j in range(2,n+1):
        if n%j== 0:
            break
    if j==n: 
        return 1 
    else:
        return 0
lst=eval(input())
a=[]
for i in lst:
    if issu(i):
        a.append(i)
print(a)


