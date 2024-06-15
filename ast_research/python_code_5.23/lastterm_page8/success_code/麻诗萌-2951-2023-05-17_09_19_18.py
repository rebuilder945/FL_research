def matrix(n=2): 
    if n==2:
        print("*","*")
        print("*","*")
    else:
        lst=["*"]*n
        for i in range(n):
            print(" ".join(lst))


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(int(number))  #有实参调用自定义函数

