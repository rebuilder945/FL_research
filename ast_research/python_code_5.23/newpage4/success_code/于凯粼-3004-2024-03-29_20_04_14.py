def isPrime(n):
    for i in range (2,n):
        if n%i ==0:
            return False
    return True
numbers=eval(input())
result=[]
for n in numbers:
    if isPrime(n):
        result:append(n)
print(result)

