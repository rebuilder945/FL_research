def Fibonacci(x,y):
    if y<=2:
        return 1
    else:
        return Fibonacci(x,y-1)+Fibonacci(x,y-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


