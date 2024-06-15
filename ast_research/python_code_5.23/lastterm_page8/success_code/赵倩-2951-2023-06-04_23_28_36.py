def matrix(n=2): 
    for x in range(n):
        for y in range(n):
            print('*',end=" ")
        print("\n")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

