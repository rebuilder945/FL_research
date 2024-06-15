def isPrime(num):
    if num < 2:
        return False
    else:
        isPrime = True
        for i in range(2,num):
            if num % i == 0:
                isPrime = False
        return isPrime


lst = eval(input())
lst1 = []
for i in lst:
    if isPrime(i):
        lst1.append(i)
print(lst1)



