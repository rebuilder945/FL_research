def Fibonacci():
    global num, n
    #定义的 Fibonacci() 函数没有参数，但是在调用时却传入了两个参数 num 和 n。
    #将 num 和 n 定义为全局变量
    for i in range(n-2):
        a = num[-1] + num[-2]
        num.append(a)

num = [1, 1]
n = int(input())
Fibonacci()
print(num)