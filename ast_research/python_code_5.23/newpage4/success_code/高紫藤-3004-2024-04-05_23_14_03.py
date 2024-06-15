# import math
# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range (2,n):
#         if n % i == 0:
#             return False
#     return True
# numbers = eval(input())
# result = []
# for n in numbers:
#     if isPrime(n):
#         result.append(n)
# print(result)


def Prinm(n):
    if n <= 1:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
        return True
a = eval(input())
b = []
for n in a:
    if Prinm(n):
        b.append(n)
print(b)












