import math
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
            if num % i ==0:
                return False
    return True

numbers=eval(input())
result=[]
for num in numbers:
    if is_prime(num):
        result.append(num)

print(result)
