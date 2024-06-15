def matrix(n=2): 
    if n=="0":
        print(("*"*2)*2)
    else:
        print("*"*n)*n)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

