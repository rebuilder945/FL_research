def matrix(n=2): 
    for in range(n):
        for j in range(n):
            print("*",end=" ")
        print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    maxtrix(eval(number))  #有实参调用自定义函数

