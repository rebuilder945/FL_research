def matrix(n=2): 
    for r in range(n):
        for c in range(n):
           print("*",end=" ")
    print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

