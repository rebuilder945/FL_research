def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

n = input()
if '.' in n or '-' in n:
    print("illegal input")
else:
    n = int(n)
    result = []
    for i in range(2, n+1):
        if is_prime(i) and is_palindrome(i):
            result.append(str(i))
    print(' '.join(result))
