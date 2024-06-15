import math

def isPrime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def reverseNumber(n):
    num = str(n)
    m = num[::-1]
    if num == m:
        return n

N = float(input())
if (N - int(N)) > 0:
    print("illegal input")
elif int(N) < 1:
    print("illegal input")
else:
    N = int(N)
    hui = []
    for x in range(2, N):
        if isPrime(x) and reverseNumber(x) == x:
            hui.append(x)
    for x in range(len(hui)):
        print("%d" % hui[x], end=' ')
        #在 print 函数中的 end 参数的值不正确导致的，end 参数应该是一个字符串，用于指定在输出结束时添加到输出的字符，
        #但传递了一个空列表 end=''.split()，这是不合法的。
        #如果想要将输出与空格分隔开，可以简单地将 end 参数设置为一个空格字符串 ' '。