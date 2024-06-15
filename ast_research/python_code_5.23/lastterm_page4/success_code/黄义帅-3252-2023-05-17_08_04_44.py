def  Fibonacci(lst,n):
       for i in range(2,n):
             lst.append(lst[i-1]+lst[i-2])
       return lst[-1]
       




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


