def matrix(n=2): 
    a = "*"*n**2
    for i in range(n):
        if i!=n*i+1:
           print(a[i],end="")
        else:
           print(a[i])

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
     matrix(number)  #有实参调用自定义函数

