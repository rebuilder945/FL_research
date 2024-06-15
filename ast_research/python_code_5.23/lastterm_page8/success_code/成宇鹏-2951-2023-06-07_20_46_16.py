def matrix(n=2): 
        ls = ["*"]*int(n)
        for i in range(int(n)):
            print(*ls,sep=' ')


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

