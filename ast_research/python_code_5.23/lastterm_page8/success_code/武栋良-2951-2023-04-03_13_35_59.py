def matrix(n=2): 
    a = [["*"]*n]*n
    print(a)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
     matrix(number)  #有实参调用自定义函数

