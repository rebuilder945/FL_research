def is_prime(n):
    if n > 1:
        for i in range (2, n):
            if n % i == 0:
                return False
        return True
    else:  # 对于 n <= 1 的情形，返回 False
        return False

def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

N = float(input())
if N - int(N) > 0 or N < 1:
    print("illegal input")
else:
    N = int(N)
    sums = []
    for i in range(2, N):
        if is_prime(i) and is_palindrome(i):
            sums.append(i)
    print(sums)  # 输出所有符合条件的回文质数
