import math  #从Python标准库中引入math.py模块，这是Python中定义的引入模块的方法
def mowei(y,n,m):
    #if n!=math.floor(n):  #将数字向下舍入到最接近的整数
    if n not in y:
        print('error')
    else:
        if n>=(-len(y)) and n<len(y):
            x=y[n]
            for i in range(m):
                y.append(x)
            print(y)
        else:
            print('error')
            
sums=list(eval(input()))  #输入列表，sums即为列表的名字
n,m=eval(input())
mowei(sums,n,m)  #把三个传到函数

