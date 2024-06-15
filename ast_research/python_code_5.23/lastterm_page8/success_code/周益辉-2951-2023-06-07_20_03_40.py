def matrix(n=2): 
            str1=''
            for i in range(n):
                str1+='* '
            str1.strip()
            for i in range(n):
                print(str1)
        

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

