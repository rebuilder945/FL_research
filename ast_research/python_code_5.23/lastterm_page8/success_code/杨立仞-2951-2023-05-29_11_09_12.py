def matrix(n=2): 
    n=int(n)
    a=['*']*n
    b=" ".join(a)
    for x in range(n):
        print(b)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

