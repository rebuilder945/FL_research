def matrix(n=2): 
    ju=[["*" for x in range(n)] for y in range(n)]
    for i in ju:
            print(" ".join(i))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

