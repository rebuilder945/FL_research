def matrix(n=2): 
    a=int(n)*"*"
    b=" ".join(a)
    c=1
    while c<=int(n):
        print(b)
        c+=1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

