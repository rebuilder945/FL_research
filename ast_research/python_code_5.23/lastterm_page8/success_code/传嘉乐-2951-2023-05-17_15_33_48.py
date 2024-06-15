def matrix(n=2): 
    for x in range(int(n)):
            for x in range(int(n)):
                print('*',sep=' ')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

