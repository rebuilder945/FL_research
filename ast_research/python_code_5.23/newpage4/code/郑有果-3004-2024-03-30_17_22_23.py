def sieve_of_eratosthenes:
    primes = list()
    sieve = [True] * (n+1)
    for current_prime in range(2, int(n**0.5)+1):
        if sieve[current_prime]:
            for multiple in range(current_prime*current_prime, n+1, current_prime):
                sieve[multiple] = False
    for current_prime in range(2, n+1):
        if sieve[current_prime]:
            primes.append (current_prime)
    return primes

input_list =eval(input())
output_list = sieve_of_eratosthenes(max(input_list))
print(output_list)
