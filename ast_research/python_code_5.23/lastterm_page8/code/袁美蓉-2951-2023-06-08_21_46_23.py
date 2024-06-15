def matrix(n=2): 
    return [* for r in range(2)] for c in range(2)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n)  #有实参调用自定义函数

