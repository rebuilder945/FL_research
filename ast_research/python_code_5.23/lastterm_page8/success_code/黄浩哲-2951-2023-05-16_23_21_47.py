def matrix(n=2): 
            string=''
            for i in range(n-1):
                string += '* '
            string += '*'
            for j in range(n):
                print(string)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

