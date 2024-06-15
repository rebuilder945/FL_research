def matrix(n=2): 
    a=n
    while n >0:
        print('* '*a,end='\n')
        n=n-1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=int(number))  #有实参调用自定义函数

