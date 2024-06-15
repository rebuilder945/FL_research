def matrix(n=2): 
    s=["*"]
    for i in range(n-1):
        s+=s
    ls1=[]
    for j in range(n):
        ls1.append(s)
    for x in range(n):
        for y in range(n):
            print(ls1[x][y],end='')

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=eval(number))  #有实参调用自定义函数

