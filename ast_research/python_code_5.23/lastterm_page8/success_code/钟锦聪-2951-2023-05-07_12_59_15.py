def matrix(n=2): 
        for i in range (n**2):
            if i % n!= 0:
                print ("{:<2}". format ("*"), end ="") 
            else :
                print()
                print ("{:<2}". format ("*"), end ="") 

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=int(number))  #有实参调用自定义函数

