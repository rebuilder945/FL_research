def Fibonacci(biao,shu):
    i=1
    while i<(shu-1):
        he=biao[i-1]+biao[i]
        biao.append(he)
        i+=1
    return biao[(shu-1)]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


