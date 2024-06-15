def matrix(n=2): 
    for i in range(1,n+1):
        for j in range(i,n+1):
            print('*',end=' ')
        print('\n')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

