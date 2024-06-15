import math
def isprime(num):
    if num<0 or num in (0,1):
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
lit=eval(input())
out=[]
for i in range(len(lit)):
    if isprime(lit[i]):
        out.append(lit[i])
print(out)
