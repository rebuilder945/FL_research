def su(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    if n==1:
        return 0    
    return 1
a=eval(input())
b=[]
for i in range(len(a)):
    if su(a[i])==1:
        b.append(a[i])
    else:
        pass
print(b)
