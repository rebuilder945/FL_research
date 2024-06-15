def matrix(n=2): 
    n = int(n)
    a = "*"*n**2
    for x in range(n**2):
        b = [n*i-1 for i in range(1.,n+1)]
        if x in b
            print(a[x])
        else:
            print(a[x],end=" ")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
     matrix(number)  #有实参调用自定义函数

