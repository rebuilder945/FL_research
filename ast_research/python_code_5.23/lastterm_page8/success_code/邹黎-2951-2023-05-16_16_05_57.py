def matrix(n=2): 
    c=0
    str=""
    while True:
        if c ==n:
           break
        else:
           str+="* "
           c+=1
    print(str)
        

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

