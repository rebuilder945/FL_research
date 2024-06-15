def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def palindrome(num):
    return str(num) == str(num)[::-1]

n = input()
if not n.isdigit() or int(n) <= 1:
    print('illegal input')
else:
    n = int(n)
    result = []
    for i in range(2, n + 1):
        if prime(i) and palindrome(i):
            result.append(str(i))
    print(' '.join(result))
