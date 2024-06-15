def is_prime(num):
    """判断一个数是否为素数"""
    if num <= 1:  # 小于等于1的数不是素数
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # 有其他因数，不是素数
            return False
    return True
def is_palindrome(num):
    """判断一个数是否为回文数"""
    str_num = str(num)
    return str_num == str_num[::-1]
n = input()
if not n.isdigit() or int(n) <= 1:  # 输入不合法
    print("illegal input")
else:
    n = int(n)
    result = []  # 记录回文素数
    for i in range(2, n+1):
        if is_prime(i) and is_palindrome(i):
            result.append(str(i))
    print(" ".join(result))  # 输出结果，用空格分隔
