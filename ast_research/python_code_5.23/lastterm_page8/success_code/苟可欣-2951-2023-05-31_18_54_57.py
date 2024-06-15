def matrix(n=2): 
    for x in range(n-1):
        print(["*"*n],end=" ")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n)  #有实参调用自定义函数

