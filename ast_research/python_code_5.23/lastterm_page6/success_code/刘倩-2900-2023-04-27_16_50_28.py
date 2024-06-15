def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n ** 0.5) +1):
        if n%i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n == str(n)[::-1])

n = eval(input())
if not n.isdigit() or n<=1:
    print("illegal input")
else:
    palindromic_primes = []
    for i in range(2,n+1):
        if is_prime(i) and is_palindrome(i):
            palindromic_primes.append(i)
    print(" ".join(palindromic_primes))
