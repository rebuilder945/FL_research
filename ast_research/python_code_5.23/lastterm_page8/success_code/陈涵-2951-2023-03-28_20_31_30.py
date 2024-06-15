def matrix(n=2): 
    m=['*' for i in range(n)]
    for i in range(n):
        print(" ".join(m))  

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(str(number))  #有实参调用自定义函数

