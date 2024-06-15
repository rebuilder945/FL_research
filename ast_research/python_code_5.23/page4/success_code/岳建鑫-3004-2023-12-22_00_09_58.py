def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(nums):
    prime_list = []
    for num in nums:
        if is_prime(num):
            prime_list.append(num)
    return prime_list

input_str = input()
nums = eval(input_str)
prime_list = find_prime_numbers(nums)
print(prime_list)

