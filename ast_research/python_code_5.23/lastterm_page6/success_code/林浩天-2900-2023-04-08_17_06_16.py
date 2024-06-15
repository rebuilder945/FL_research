import math
def isPrime(n):
    if n > 1 :
        for i in range(2, n):
            if n % i == 0:
                return 0
    return 1

def reverseNumber(n):
    num = str(n)
    m = num[::-1]
    if num == m:
        return n
N = float(input())
if (N-int(N))>0:
    print("illegal input")

elif int(N)<1:
    print("illegal input")
else:
    N=int(N)
    hui=[]
    m=2
    for x in range(2,N):
        if isPrime(x) and reverseNumber(x) == x:
            hui.append(x)
    for x in range(len(hui)):
        print("%d "%hui[x],end='')
#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303
