def isPrime(num):
    for i in range(2, num//2+1):
        if( num%i == 0):
            return False
    return True

lst=eval(input())
a=[]
for i in lst:
    if i==0:
        lst.remove(0)
    elif i==1:
        lst.remove(1)
    if isPrime(i):
        a.append(i)
print(a)


