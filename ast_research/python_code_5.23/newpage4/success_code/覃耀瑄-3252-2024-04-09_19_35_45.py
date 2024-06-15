Fibonacci=[1,1]
n  =  int(input())
while len(Fibonacci)<n+1:
          n=Fibonacci[-1]+Fibonacci[-2]
          Fibonacci.append(n)





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


