def matrix(n=2): 
    if str(n).isdigit():
       for i in range(n):
           for j in range(n):
                if  j == n-1:
                     print('*')
                else:
                     print('*', end=' ')
    else:
        for i in range(2):
           for j in range(2):
                if  j == 1:
                     print('*')
                else:
                     print('*', end=' ')
                   


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

