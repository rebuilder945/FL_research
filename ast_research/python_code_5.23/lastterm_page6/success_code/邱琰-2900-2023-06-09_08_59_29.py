import math
def isPrime(num):
    if num<0 or num in (0,1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return num
def huiwen(n):
    s=str(n)
    if s==s[::-1]:
        return True
    else:
        return False
n=eval(input())
ls=[]
for i in range(1,int(n)+1):
    if huiwen(i) and isPrime(i):
        ls.append(i)
if len(ls)==0:
    print('illegal input')
else:
    print(*ls)
