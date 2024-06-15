def Fibonacci(a, i):
    a = 1
    b = 2
    for x in range(i - 2):
        c = a + b
        a = b
        b = c
    return c

n = eval(input())
d = []
for i in range(n):
    m = Fibonacci(i + 2, n) / Fibonacci(i + 1, n)
    #函数 Fibonacci() 需要两个参数 a 和 i，但是在调用时没有传递 a 参数
    d.append(m)
e = sum(d)
print("%.4f" % e)
