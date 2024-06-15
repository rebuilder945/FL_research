#回文素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = input()
if not n.isdigit() or int(n) <= 1:
    print("illegal input")
else:
    print(" ".join(str(i) for i in range(2, int(n) + 1) if is_prime(i) and is_palindrome(i)))
