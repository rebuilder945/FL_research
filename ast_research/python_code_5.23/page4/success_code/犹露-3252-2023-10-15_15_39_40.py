
def Fibonacci(q,  w):
    a1 = q[0]
    a2 = q[1]
    for i in range(w-1):
        a1,a2 = a2,a2+a1
    return a1




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


