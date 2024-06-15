def matrix(n=2): 
    i=0
    hang="* "*n
    while i<n:
        print(hang)
        i+=1

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

