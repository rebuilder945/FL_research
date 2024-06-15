def matrix(n=2): 
    for x in range(n):
        for y in range(n):
            print('*',end=' ')
            if y ==n-1:
                print('\n')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

