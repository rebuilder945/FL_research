def matrix(n=2): 
    a=numpy.zeros(shape(n,n))
    for i in n:
        a[i]='*'

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=eval(number))  #有实参调用自定义函数

