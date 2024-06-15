visit = {}
def Fibonacci(num,n):
      if n==1 or n==2:
            return 1
      else:
        if n in visit.keys():
            return visit[n]
        else:

            temp = Fibonacci(num,n-2)+Fibonacci(num,n-1)
            visit[n] = temp
            return temp




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


