def matrix(n=2): 
    x=n
    while x>0:
        for i in range(n):
            print('*',end=' ')
        x-=1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

