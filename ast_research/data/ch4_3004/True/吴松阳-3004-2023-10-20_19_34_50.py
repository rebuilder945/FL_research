def prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
num = eval(input())
primelist = []
for n in num:
    if prime(n):
        primelist.append(n)
print(primelist)
