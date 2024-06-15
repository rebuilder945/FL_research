def matrix(n=2): 
    lst=['*']*n
    for x in range(n):
        print(" ".join(lst))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

