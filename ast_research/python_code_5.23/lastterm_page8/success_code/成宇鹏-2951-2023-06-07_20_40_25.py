def matrix(n=2): 
        ls = "*"
        ls1 = ls*n
        for x in range(n):
            print(*ls1,sep=' ')
     

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

