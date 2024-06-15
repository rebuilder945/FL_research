def Fibonacci(x,y):
         a = num[0]
         b = num[1]
         for i in range(y-2):
         a,b = b,a+b
         return(b)





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


