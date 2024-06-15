def matrix(n=2): 
        for x in list(range(int(n))):
            for y in list(range(int(n))):
                print("*",end=' ')
        print("")


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
       matrix(n=number)  #有实参调用自定义函数

