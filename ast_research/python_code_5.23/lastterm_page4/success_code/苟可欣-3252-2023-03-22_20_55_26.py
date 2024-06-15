Fibonacci=[1,1]
for x in range(2,100):
    a=sum(Fibonacci[x-2:x])
    Fibonacci.append(a)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


