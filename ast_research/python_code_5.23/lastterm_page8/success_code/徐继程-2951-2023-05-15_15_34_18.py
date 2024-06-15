def matrix(n=2): 
        a='' 
        for i in range(n):
            a+='* '
        for i in range(n):
            print(a)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

