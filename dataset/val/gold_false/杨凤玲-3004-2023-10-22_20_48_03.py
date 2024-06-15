def is_prime(a):
    if a <= 2:
        return a
    else:
        for i in range(2,a):
            if a % i== 0:
                return False
            else:
                return a
b = eval(input())
prime_list = []
for c in b:
    if is_prime(c):
        prime_list.append(c)
print(prime_list)
