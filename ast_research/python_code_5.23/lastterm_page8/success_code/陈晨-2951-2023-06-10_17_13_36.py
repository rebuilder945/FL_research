def matrix(n=2): 
    k=0
    while k!=n:
        k+=1
        print("* "*int(n))

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

