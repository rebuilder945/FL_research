def matrix(n=2): 
    a="*"
    for i in range(n-1):
        a+=" *"
    for i in range(n-1):
        print(a)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=eval(number))  #有实参调用自定义函数

