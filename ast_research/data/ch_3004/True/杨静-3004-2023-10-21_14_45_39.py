ls1 = eval(input())
ls3 = []
for x in ls1:
    if x <= 1:
        continue
    is_prime = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        ls3.append(x)
print(ls3)
