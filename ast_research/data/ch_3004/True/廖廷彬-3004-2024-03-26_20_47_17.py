def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
input_list_str = input()
input_list = eval(input_list_str)
prime_list = [num for num in input_list if is_prime(num)]
print(prime_list)
