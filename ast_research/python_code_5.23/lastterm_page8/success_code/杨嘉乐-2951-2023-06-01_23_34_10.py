def matrix(n=2): 
    if isinstance(n,int):
        nn=n
    else:
        nn=eval(n)
    for i in range(nn):
        for j in range(nn):
            print("*",end=" ")
        print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

