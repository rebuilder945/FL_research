def isprime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def ispalindrome(x):
    p = x 
    k = 0
    while p != 0:
        k = k*10 + p%10
        p = p//10
    if k == x:
        return True
    else:
        return False

a = eval(input())
for i in range(a):
    if isprime(a) == 1 and ispalindrome(a):
        print(a)

