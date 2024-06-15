def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False 
    return True
numbers=eval(input())
prime_list = []
for num in numbers:
    if is_prime(num):
        prime_list.append(num)
print(prime_list)


