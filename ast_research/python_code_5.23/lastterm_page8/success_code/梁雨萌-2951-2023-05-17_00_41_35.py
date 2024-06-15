def matrix(n=2): 
        lis = [["*"]*(n)]*(n)
        print(lis)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
            matrix(number)  #有实参调用自定义函数

