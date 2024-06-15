def matrix(n=2): 
    for i in list(range(int(n))):
        for j in list(range(int(n))):
            print("*",end="")
        print("")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
      #有实参调用自定义函数

