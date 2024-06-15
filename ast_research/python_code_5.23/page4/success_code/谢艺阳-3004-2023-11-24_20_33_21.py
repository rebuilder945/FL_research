import math
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
h=eval(input())
s=[]
for n in h:
    if isPrime(n):
        s.append(n)
print(h)
