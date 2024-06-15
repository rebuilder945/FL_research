def matrix(n=2): 
    if n==2:
        print("* *")
        print("* *")
    else:
        for i in range(n):
            for j in range(n):
                print("* ",end="")
            print("\n")


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

