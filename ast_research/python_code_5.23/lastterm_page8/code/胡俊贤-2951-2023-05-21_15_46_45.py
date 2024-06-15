def matrix(n=2): 
    for i in range(n):
        for i in range(n-1):
            print('*',end=' ')
        print('*',end=/n)
        

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

