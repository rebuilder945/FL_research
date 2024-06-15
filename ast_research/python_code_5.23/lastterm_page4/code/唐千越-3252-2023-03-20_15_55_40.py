def Fibonacci(num,  n):
x=num[-1:-2]
y=num[-2:-3]
z=x+y
num.append(z)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


