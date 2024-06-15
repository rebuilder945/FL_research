def matrix(n=2): 
        for x in range(n):
            a="*"*5
            print(" ".join(a))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

