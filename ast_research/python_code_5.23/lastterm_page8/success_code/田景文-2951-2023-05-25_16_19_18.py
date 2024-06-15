def matrix(n=2): 
        r = '* ' * n
        for i in range(n):
            print(r)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
        matrix(n=int(number))      #有实参调用自定义函数

