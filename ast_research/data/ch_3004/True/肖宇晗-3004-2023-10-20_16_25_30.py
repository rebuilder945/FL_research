def find_primes(nums):
    results = []
    for num in nums:
        is_primes = True
        for i in range(2,num):
            if num%i ==0:
                is_primes = False
                break
        if is_primes and num >1:
            results.append(num)
    return results
nums=eval(input())
print(find_primes(nums))
