def matrix(n=2): 
    a=['*']*n
    b=' '.jion(a)+'/n'
    c=''"
    for i in range(n):
        c+=b
    return c

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

