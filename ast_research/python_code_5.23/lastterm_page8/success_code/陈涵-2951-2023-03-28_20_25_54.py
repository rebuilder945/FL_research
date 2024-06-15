def matrix(n=2): 
    num=[['*' for i in range(n)] for j in range(n)]
    print(num)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

