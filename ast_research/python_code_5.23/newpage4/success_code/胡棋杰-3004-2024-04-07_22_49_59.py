def 素数(n):
    for i in range(2,n//2+1):
       if n%i==0:
           return False
    return True
a=eval(input())
k=[]
for i in a:
    if 素数(i):
        k.append(i)
print(k)


