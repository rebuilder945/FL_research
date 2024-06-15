def matrix(n=2): 
    try:
        for i in range(n):
            for j in range(n):
                print("*",end = " ")
            print("\n")
    except ValueError as e:
        print("* *\n")
        print("* *")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

