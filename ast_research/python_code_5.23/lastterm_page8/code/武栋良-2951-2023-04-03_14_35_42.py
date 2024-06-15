def matrix(n=2): 
    n = int(n)
    a = "*"*n**2
    for x in range(n**2):
        b = [n*i for i in range(1:n)]
        if x not in b:
            print(a[x],end=" ")
        else:
            print(a[x])

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
     matrix(number)  #有实参调用自定义函数

