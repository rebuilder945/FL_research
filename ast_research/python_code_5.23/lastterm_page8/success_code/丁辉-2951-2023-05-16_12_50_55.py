def matrix(n=2): 
    a=[['*' for c in range(n)] for r in range(n)]
    for r in range(n):
        for c in range(n):
            print(a[r][c],end=' ')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

