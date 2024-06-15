def find_primes:
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n+1, p):
                is_prime[i] = False
        p += 1

    primes = [p for p in range(2, n+1) if is_prime[p]]
    return primes

nums = list(map(int, input().split()))
primes = find_primes(max)
print(primes)
