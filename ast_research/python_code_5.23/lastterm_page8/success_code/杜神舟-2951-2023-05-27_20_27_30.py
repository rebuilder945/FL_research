def matrix(n=2): 
        ls=[]
        for x in range(int(n)):
            ls.append('*')
        for x in range(int(n)):
            print(' '.join(ls))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
        matrix(number)  #有实参调用自定义函数

