def matrix(n=2): 
            a=""
            for i in range(n):
                    print(a,end='\n')
                    for x in range(n):
                            a+="*"

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

