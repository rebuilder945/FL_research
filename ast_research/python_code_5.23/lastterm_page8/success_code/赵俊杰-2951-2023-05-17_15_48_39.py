def matrix(n=2): 
    for r in range(n):
        for c in range(n):
           print("*",end=" ")
        print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=int(number))  #有实参调用自定义函数

