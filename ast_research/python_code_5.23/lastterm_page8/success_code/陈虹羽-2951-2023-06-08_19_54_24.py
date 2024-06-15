def matrix(n=2): 
        c=[]
        for i in range(int(n)):
            for x in range(int(n)):
                c.append('*')
            print(' '.join(c))
            c=[]

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)   #有实参调用自定义函数

