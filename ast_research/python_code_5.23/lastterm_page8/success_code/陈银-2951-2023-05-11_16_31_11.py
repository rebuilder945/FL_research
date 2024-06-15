def matrix(n=2): 
    if int(n) !=2 :
        for i in range(int(n)):
            for j in range(int(n)):
                print("*",end=" ")
            print()
    else:    
        for i in range(2):
            for j in range(2):
                print("*",end=" ")
            print()

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

