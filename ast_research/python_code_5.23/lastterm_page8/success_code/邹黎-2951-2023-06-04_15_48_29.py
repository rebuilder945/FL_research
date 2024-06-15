def matrix(n=2): 
    
    lst=[["*" for x in range(n)] for y in range(n)]
    for x in lst:
        print(" ".join(x))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

