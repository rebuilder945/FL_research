def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
nums=eval(input())
primes=[]
for num in nums:
    if is_prime(num):
        primes.append(num)
print(primes)
