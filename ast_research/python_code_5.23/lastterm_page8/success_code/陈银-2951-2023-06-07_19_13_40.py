def matrix(n=2): 
    if int(n)==2:
        for x in range(2):
            for y in range(2):
                print("*",end=" ")
            print()
    else:
        for x in range(n):
            for y in range(n):
                print("*",end=" ")
            print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

