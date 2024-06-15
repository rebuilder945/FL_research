def Fibonacci(x,y):
    if y>2:
        for a in range(y-2):
            b=x[-1]+x[-2]
            x.append(b)
        return x[-1]
    elif y==1 or y==2:
        return 1




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


