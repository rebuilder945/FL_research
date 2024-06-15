def matrix(n=2): 
        a=m=n
        while n>0:
            m=a
            while m>0:
                if m>1:
                    print('*',end=' ')
                    m-=1
                else:
                    print('*',end='\n')
                    m-=1
            n-=1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=eval(number))  #有实参调用自定义函数

