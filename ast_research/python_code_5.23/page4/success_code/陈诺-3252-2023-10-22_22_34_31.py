#第一种：
def Fibonacci(num,n):
    n_2 = 0
    n_1 = 1
    current  = 1
    for x in range(2, n+1):
        current = n_2 + n_1
        n_2 = n_1
        n_1 = current
    return current
# print('第%d个数是%d'%(n, current))
num  =  [1,  1]
n  =  int(input())
print(Fibonacci(num,  n))





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


