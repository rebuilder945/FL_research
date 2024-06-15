lst = eval(input())
lst1 = []
for x in lst:
    if x == 2:
        lst1.append(x)
    elif x > 2:
        is_prime = True
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            lst1.append(x)
print(lst1)
