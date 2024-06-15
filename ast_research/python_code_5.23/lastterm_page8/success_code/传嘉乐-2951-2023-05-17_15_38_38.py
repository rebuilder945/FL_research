def matrix(n=2): 
        i=0
        while i<n: 
            for x in range(int(n)):
                print('*',end=' ')
                i+=1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

