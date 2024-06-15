def matrix(n=2): 
    for x in range(2):
        for i in range(2):
            print("*",end=" ")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

