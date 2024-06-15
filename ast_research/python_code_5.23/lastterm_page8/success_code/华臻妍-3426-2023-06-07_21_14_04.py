import math#有开根号函数，引入math包
def f(x):
    if x<20:
        y=6*x**2+1
    elif 20<=x<40:
        y=math.sqrt(3*x-60)
    else:
        y=100/(x+1)
    return y
#构造输入和输出
x=eval(input())
y=f(x)
print("%.2f"%y)
