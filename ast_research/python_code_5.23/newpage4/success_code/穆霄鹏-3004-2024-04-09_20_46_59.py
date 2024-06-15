def hh(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return True
    return True
numbers=eval(input())
result=[]
for n in numbers:
    if hh(n):
        result.append(n)
print(result)
