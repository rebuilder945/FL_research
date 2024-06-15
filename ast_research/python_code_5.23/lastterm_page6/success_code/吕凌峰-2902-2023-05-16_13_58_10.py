# 数列求和
# 【问题描述】有一个分数数列：2/1,3/2,5/3,8/5,13/8,21/13,...
# 从键盘输入一个正整数n，求出这个数列的前n项之和

def Fibonacci(y):
    x = [1, 1]
    for y in range(1,y):
        if y > 1:
            c = x[y - 2] +x[y - 1]
            x.append(c)
        else:
            pass
    return x[-1]
def sum_calculate(n):
    Sum = 0
    for i in range(n):
        Sum += (Fibonacci(i + 3)) / (Fibonacci(i + 2))
    return '%.4f' %Sum
num = eval(input())
print(sum_calculate(num))
