def matrix(n=2): 
    for i in range(1,n+1):
        num=1
        for x in range(n):
            if num<i:
                print('*',end='')
                num+=1
            else:
                print('*',end='')
         print()
        

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    maxtrx(n=int(number))  #有实参调用自定义函数

