import math
def isPrime(n):
    if n<= 1:
        return False
    return True
numbers = eval(input())
result = []
for n in numbers:
    if isPrime(n):
        result.append(n)
print(result)
