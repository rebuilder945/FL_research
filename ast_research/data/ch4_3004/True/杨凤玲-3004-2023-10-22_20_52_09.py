def is_prime(a):
    if a==1:
        return  False
    if a == 2:
        return a
    if a==9:
        return False
    if a==27:
        return False
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
