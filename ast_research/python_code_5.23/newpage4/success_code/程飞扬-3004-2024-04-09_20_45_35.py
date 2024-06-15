def isPrime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
b=eval(input())
if 0 in b:
    b.remove(0)
if 1 in b:
    b.remove(1)
a=[]
for i in b:
    if isPrime(i):
        a.append(i)
print(a)

