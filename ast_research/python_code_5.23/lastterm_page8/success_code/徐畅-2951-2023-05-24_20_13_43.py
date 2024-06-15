def matrix(n=2): 
        a=["*"]*n
        for x in range(n):
               print(*a,sep=' ')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
            matrix(eval(number))  #有实参调用自定义函数

