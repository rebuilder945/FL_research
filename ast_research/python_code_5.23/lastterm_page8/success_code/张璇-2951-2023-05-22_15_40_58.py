def matrix(n=2): 
            a="*"*n
            print(a,sep=n)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

