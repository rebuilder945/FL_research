def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

input_list = [2, 3, 5, 7, 9, 11, 23]
prime_list = [x for x in input_list if is_prime(x)]
print(prime_list)

