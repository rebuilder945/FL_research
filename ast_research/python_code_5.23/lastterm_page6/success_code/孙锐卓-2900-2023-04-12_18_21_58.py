import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    str_num = str(num)
    for i in range(len(str_num)//2):
        if str_num[i] != str_num[len(str_num)-1-i]:
            return False
    return True

n = input()
if not n.isdigit() or int(n) < 2:
    print("illegal input")
else:
    for i in range(2, int(n)):
        if is_prime(i) and is_palindrome(i):
            print(i, end=" ")





