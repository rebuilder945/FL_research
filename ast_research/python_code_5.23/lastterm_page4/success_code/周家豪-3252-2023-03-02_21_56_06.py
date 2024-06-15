def Fibonacci(new,  total):
    for i in range(2,total):
        new=num[i-1]+num[i-2]
        num.append(new)
    return new
    





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


