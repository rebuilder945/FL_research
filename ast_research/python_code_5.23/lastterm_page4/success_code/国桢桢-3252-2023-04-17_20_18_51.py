def Fibonacci(num,  n):
 num = [1,1]
 a = 1
 b = 1
 if n < 3:
  return ("1")
 else:
  for i in range(n):
   a,b = b,a+b
   num.append(b)
  return(num[-1])





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


