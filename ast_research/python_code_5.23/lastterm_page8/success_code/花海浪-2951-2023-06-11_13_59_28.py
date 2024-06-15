def matrix(n=2): 
    for i in range(n):
            print(" ".join("*"*n))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

