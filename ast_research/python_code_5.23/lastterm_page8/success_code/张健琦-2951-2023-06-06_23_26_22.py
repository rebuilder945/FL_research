def matrix(n=2): 
            a='* '*n
            for i in range(n):
                print(a)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

