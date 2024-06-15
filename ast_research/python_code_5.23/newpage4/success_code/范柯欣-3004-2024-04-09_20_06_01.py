def isPrime(num):
    for i in range(2, num//2+1):
        if( num%i == 0):
            return False
    return True

lst=eval(input())
if 0 in lst:
    lst.remove(0)
if 1 in lst:
    lst.remove(1)
a=[]
for i in lst:
    if isPrime(i):
        a.append(i)
print(a)


