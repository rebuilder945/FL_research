def matrix(n=2): 
        n=number
        b=['*']*n
        c=' '.join(b)
        for i in range(n):
            print('\t',c)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

