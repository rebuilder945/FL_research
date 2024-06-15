def matrix(n=2): 
    for i in range(n):
            for j in range(x):
                print("*",end="")
            print("/n")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

