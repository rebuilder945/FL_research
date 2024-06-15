def matrix(n=2): 
    for x in range(n):
        b=["*"for x in range(n)]
        print( " ".join(b))


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=int(number))  #有实参调用自定义函数

