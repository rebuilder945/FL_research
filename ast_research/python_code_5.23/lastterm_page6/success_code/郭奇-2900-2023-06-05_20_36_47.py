def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = eval(input())
if n < 0 or n % 1 != 0:
    print('illegal input')
else:
    lst1 = []
    lst2 = []
    for i in range(2, n):
        if is_prime(i):
            lst1.append(i)
    for i in range(len(lst1)):
        m = len(str(lst1[i]))
        is_palindrome = True
        for x in range((m-1)//2):
            if lst1[i][x] != lst1[i][-x-1]:
                is_palindrome = False
                break
        if is_palindrome:
            lst2.append(lst1[i])
    if len(lst2) == 0:
        print("No prime palindromes found.")
    else:
        print(lst2)
