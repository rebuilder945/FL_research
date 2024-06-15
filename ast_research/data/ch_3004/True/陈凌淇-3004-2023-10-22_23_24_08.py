def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

# 输入列表
input_str = input()
try:
    # 从字符串中解析列表
    num_list = eval(input_str)
    prime_list = [x for x in num_list if is_prime(x)]
    print(prime_list)
except:
    print("输入无效，请确保输入合法的列表格式。")

