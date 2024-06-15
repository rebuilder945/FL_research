def Fibonacci(seq,ls):
    ls1,ls2,ls3 = 1,1,0
    while ls > 2:
        ls3 = ls1 +ls2
        ls1, ls2 = ls2, ls3
        ls = ls - 1
    return ls3




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


