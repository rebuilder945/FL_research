def is_palindrome(num):
    """判断一个数是否为回文数"""
    str_num = str(num)
    return str_num == str_num[::-1]

def is_prime(num):
    """判断一个数是否为素数"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = input()

if "." in n or int(n) < 1:
    print("illegal input")
else:
    n = int(n)
    palindrome_primes = []
    for i in range(2, n+1):
        if is_palindrome(i) and is_prime(i):
            palindrome_primes.append(str(i))
    print(" ".join(palindrome_primes))

