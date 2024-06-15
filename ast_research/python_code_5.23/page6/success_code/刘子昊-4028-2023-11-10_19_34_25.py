def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    try:
        n = int(input())
        if n <= 1:
            print("illegal input")
            return

        palindrome_primes = [str(x) for x in range(2, n) if is_prime(x) and is_palindrome(x)]
        result = ' '.join(palindrome_primes)
        
        print(result)

    except ValueError:
        print("illegal input")

if __name__ == "__main__":
    main()
