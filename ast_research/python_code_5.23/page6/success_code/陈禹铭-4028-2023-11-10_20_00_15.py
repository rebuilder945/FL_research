def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def is_palindrome(num):
        return str(num)==str(num)[::-1]
def palindrome_primes_up_to_n(n):
    if not isinstance(n,int) or n <=1:
        return "illegal input"
    result=[str(x) for x in range(n+1) if is_prime(x) and is_palindrome(x)]
    return " ".join(result)
try:
    user_input=int(input())
    print(palindrome_primes_up_to_n(user_input))
except ValueError:
    print("illegal input")

