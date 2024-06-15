def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a = eval(input())
result = []
for n in a:
    if isPrime(n):
        result.append(n)
print(result)
