def matrix(n=2): 
    if len(n)==0:
        print('* */n* *')
    else:
        for i in range(n):
            print('*'*(n-1)+'*')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

