def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
lst = eval(input())
lst_prime = []
for num in lst:
    if isPrime(num):
        lst_prime.append(num)
print(lst_prime)
