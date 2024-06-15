def matrix(n=2): 
    if n=="0":
        list1= [["*"]*2]*2
        print(str(list1))
    else:
        print(("*"*int(n))*int(n))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

