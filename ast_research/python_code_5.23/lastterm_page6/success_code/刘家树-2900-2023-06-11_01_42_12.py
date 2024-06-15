def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def find_palindrome_primes(n):
    if n <= 1 or not isinstance(n, int):
        print("illegal input")
        return
    
    palindrome_primes = []
    for num in range(2, n+1):
        if is_prime(num) and is_palindrome(num):
            palindrome_primes.append(num)
    
    if palindrome_primes:
        print(" ".join(map(str, palindrome_primes)))
    else:
        print("No palindrome primes found")


n = int(input())
find_palindrome_primes(n)

