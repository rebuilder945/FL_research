import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

n = input()
if not n.isdigit() or int(n) <= 1:
    print("illegal input")
else:
    n = int(n)
    res = []
    for i in range(2, n+1):
        if is_prime(i) and is_palindrome(i):
            res.append(str(i))
    print(" ".join(res))

