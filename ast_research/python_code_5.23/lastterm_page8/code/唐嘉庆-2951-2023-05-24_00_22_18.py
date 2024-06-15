def matrix(n=2): 
    string='* '*n
            for j in range(n):
                print(string)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

