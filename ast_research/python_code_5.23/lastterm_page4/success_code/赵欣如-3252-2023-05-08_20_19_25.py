def Fibonacci(x,y):
    while len(x)<y:
          a=x[-1]+x[-2]
          x.append(a)
    if len(x)==y:
          return(x[y-1])   





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


