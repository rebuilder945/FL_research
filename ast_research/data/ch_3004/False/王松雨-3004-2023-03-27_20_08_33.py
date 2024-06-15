def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n>2:
        for i in range(2,n):
            if n%i==0:
                return False
lst=eval(input())
prime_lst=[x for x in lst if is_prime(x)]
print(prime_lst)
