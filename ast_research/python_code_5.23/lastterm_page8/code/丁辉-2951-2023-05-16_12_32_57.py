def matrix(n=2): 
    a=[[* for c in range(n)] for r in range(n)]
    print(a)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

