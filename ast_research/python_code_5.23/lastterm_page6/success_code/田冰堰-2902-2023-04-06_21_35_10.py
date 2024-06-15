def f(n):
    a = 2.0
    b = 1.0
    total = 0
    for i in range(1, n + 1):
        total += a/b
        a, b = a + b, a
    print("%.4f"%total)
n=eval(input())
f(n)
