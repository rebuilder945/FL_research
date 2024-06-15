def is_prime (n):
    if n < 2:
        return False
    for i in range(2,int(n **.5)+1):
        if n % i == 0:
            return False
    return True
 
num_list = list (map(int, input().split()))
 
prime_list = []
for num in num_list:
        if is_prime (num):
            prime_list.append(num)

print(prime_list)
