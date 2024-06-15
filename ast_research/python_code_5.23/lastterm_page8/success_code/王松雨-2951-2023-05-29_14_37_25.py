def matrix(n=2): 
    for i in range(int(n)):
        for j in range(int(n)):
            print('*',end=' ')
        print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

