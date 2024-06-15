def matrix(n=2): 
    b = n**2
    a = "*"*b
    for i in range(n):
        for x in range(n**2):
            if x!=n*i+1:
               print(a[x],end="")
            else:
               print(a[x])

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
     matrix(number)  #有实参调用自定义函数

