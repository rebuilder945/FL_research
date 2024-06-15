def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

nums = eval(input())
prime_nums = [num for num in nums if is_prime(num)]
print(prime_nums)
