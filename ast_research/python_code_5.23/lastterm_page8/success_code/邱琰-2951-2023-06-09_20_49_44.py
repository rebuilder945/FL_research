def matrix(n=2): 
        s=''
        s='* '*int(n)
        while int(n)>0:
            print(s,end='\n')
            n=str(int(n)-1)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

