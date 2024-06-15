import math 
def f(n):
    if n<=1:
        return False
    for i in range(2,n)
        if n%i==0:
            return False
    else:
        return True
numbers=eval(input())
result=[]
for n in numbers:
    if f(n):
        result.append(n)
print(result)
