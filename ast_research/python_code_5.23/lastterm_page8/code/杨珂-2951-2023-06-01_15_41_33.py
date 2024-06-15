def matrix(n=2): 
    for i in range (n):
        print("*"*n\n)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

