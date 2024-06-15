def 素数(n):
 if n==2 or n==3:
    return True
 elif n<=1 or type(n)!=type(1):
    return False
 else : 
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


