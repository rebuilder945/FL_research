def is_prime(num):
    if num < 2:
        return False
    elif num==2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

input_list = eval(input())
prime_list = [x for x in input_list if is_prime(x)]
print(prime_list)

