def matrix(n=2): 
    s='*'*n
    print('s\n'*n)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

