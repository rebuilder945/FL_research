def matrix(n=2): 
    k=0
    str=""
    for x in range(int(n)):
        str+="* "
    while k!=int(n):
        k+=1
        print(str)
            

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

