def prime(n):
    if n<2:
        return False
    for i in range(2,int(n** .5)+1):
        if n % i == 0:
            return False
    return  True
def primes(lst):
    primes=[]
    for num in lst:
        if num in prime(num):
            primes.append(num)
    return primes
lst=eval(input())
primes1=primes(lst)
print(primes1)
        

