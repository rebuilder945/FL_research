def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]


n = input("n=")
if "." in n or int(n) < 0:
    print("illegal input")
else:
    for i in range(int(n)):
        if is_prime(i) and is_palindrome(i):
            print(i, end=" ")
