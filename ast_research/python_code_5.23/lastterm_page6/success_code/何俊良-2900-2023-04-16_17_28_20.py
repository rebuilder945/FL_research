def is_prime(num):
    """
    判断一个数是否为素数
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    """
    判断一个数是否为回文数
    """
    str_num = str(num)
    return str_num == str_num[::-1]


def get_palindrome_primes(n):
    """
    获取n以内的所有回文素数
    """
    if n <= 1:
        print("illegal input")
        return []

    res = []
    for num in range(2, n+1):
        if is_prime(num) and is_palindrome(num):
            res.append(num)
    return res


# 读取输入，调用函数，并输出结果
n = input().strip()
if not n.isdecimal() or int(n) < 2:
    print("illegal input")
else:
    palindrome_primes = get_palindrome_primes(int(n))
    print(" ".join(map(str, palindrome_primes)))

