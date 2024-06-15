def matrix(n=2): 
    s = ""
    if n == "":
        s = s + "*" + "*"
        for i in range(2):
            print(s)
    else:
        for i in range(n):
            s += "*"
        for i in range(n):
            print(s) 


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

