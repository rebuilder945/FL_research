def Fibonacci(x,y):
    for y in range(1,y):
        if y>1:
            c=x[y-2]+x[y-1]
            x.append(c)
        else:
            pass
    return x[y+1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


