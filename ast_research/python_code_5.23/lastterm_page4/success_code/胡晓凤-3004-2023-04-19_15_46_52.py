import math
def isPrime(num):
    if num<0 or num in (0,1):
     return False
    for i in range(2,int(math.sqrt(num))+1):
         if num%i==0:
            return False
    return True
n=eval(input())
if n%2==0 and 2<=n<22000000000:
    for p in range(2,n):
        if isPrime(p) and isPrime(n-p):
            print("%s=%s+%s"%(n,p,n-p))
            break


