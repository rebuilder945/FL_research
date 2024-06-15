import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
numbers=eval(input())
result=[]
for n in numbers:
    if isprime(n):
        result.append(n)
print(result)
