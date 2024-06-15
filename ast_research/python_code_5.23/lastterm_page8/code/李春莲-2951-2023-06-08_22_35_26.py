def matrix(n=2): 
    m=[[x for range(2)] for y for range(2)]
    print('*',end=' ')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number(input()))  #有实参调用自定义函数

