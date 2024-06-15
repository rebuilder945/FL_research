import math
lst1 = eval(input())
n = len(lst1)
lst2 = []
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
for i in range(n):
    if isPrime(lst1[i]):
        lst2.append(lst1[i])
print(lst2)
