def Fibonacci(lst,n):
    while len(lst)<=n-1:
        lst.append(lst[-1]+lst[-2])
    return lst[-1]
    





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


