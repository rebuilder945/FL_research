from math import sqrt
def isPrime(num):
    i = 2
    n=num
    if num != 1:
        while i <= sqrt(num):
            if num % i == 0 and num != 2 and num != 1:
                n=False
                break
            else:
                pass
                i=i+1
        return n
    else:
        pass
def reverseNumber(num):
    if str(num) == str(num)[::-1]:
        return num
    else:
        pass
        return False
    
            


            


N = int(input())
for n in range(1,N+1):
    if isPrime(n) and reverseNumber(n) == n:
        print(n) 


