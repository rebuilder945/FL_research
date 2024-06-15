def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    else:
        return True
 
def ispal(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
 
n = int(input())
num,a = 2,0
while a<n:
    if ispal(num) and isprime(num) :
        print(num,end=' ')
        a += 1
    num += 1

