def matrix(n=2): 
    for x in range(n):
        for y in range(n):
            print("*",end=" ")
        print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number()))  #有实参调用自定义函数

