import math
def isPrime(num):
    if num<0 or num in (0,1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return num
n=eval(input())
ls=[]
for i in n:
    if isPrime(i):
        ls.append(i)
print(ls)
