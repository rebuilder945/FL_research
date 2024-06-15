def get_prime(num):
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
ls=eval(input())
not_prime = []
is_prime = []
for i in ls:
    if get_prime(i) == False:
        not_prime.append(i)
    else:
        is_prime.append(i)
print(is_prime)
