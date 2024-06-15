def isPrime(x):
    return x != 1 and all( x%i != 0 for i in range(2,x))
def isPalindrome(x):
    return str(x) == str(x)[::-1]
def isPalindromePrime(x):
    return isPrime(x) and isPalindrome(x)
n = input()
if n.find('.') !=-1 or int(n) <= 0:
    print("illegal input")
else:
    n = int(n)
    print(*filter(isPalindromePrime, range(1,n + 1)))


