def Fibonacci (n):
    if n <= 1: 
        return n 
    else: 
        a, b = 0, 1 
    for i in range(n): 
         a, b = b, a + b 
    return a and n




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


