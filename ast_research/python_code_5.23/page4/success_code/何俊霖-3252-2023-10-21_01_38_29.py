def Fibonacci(num,n):
    F=num  # num=[1,1]
    for i in range(0,n):
        F.append(int(F[i])+int(F[i+1]))
    return F[-3]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


