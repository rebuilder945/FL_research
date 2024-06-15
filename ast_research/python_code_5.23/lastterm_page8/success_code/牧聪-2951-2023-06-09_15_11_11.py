def matrix(n=2): 
    for x in range(1,int(number)+1):
        print("* "*int(number))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

