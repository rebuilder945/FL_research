def matrix(n=2): 
    a=[]
    for i in range(n):
        a.append(" ".jion(sep("*"*n))+"\n")
    return a

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

