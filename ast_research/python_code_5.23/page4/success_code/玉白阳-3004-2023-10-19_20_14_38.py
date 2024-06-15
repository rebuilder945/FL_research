import math
def isprime(k):
    if k<=1:
        return False
    for i in range(2,k):
        if k%i==0:
            return False
    return True
numbers=eval(input())
result=[]
for n in numbers:
    if isprime(n):
        result.append(n)
print(result)


