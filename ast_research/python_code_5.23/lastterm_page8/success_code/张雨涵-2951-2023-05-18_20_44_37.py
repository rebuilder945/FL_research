def matrix(n=2): 
        if 0<n<10:
            for i in range(n):
                print("* "*n)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=eval(number))  #有实参调用自定义函数

