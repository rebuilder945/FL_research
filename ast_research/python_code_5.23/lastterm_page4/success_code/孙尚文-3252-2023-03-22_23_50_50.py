def Fibonacci(num,  n):
    for x in range(2,n):
        y=num(x-2)+num(x-1)
    num.append(y)
    return num
    

    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


