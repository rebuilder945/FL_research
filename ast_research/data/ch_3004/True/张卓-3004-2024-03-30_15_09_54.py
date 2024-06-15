input_str = input()
nums = eval(input_str)
prime_list = []
for num in nums:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
print(prime_list)

