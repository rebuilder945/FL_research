def matrix(n=2): 
    s='* '
    s=n*s
    for x in range(n):
        print(s)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

