def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(num**0.5)
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True

ist = eval(input())
ist2 = []
for num in ist:
    if is_prime(num):
        ist2.append(num)
print(ist2)
