def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

input_list = input()
input_list = eval(input_list) # 将输入字符串转换为列表

output_list = []
for num in input_list:
    if is_prime(num):
        output_list.append(num)

print(output_list)
