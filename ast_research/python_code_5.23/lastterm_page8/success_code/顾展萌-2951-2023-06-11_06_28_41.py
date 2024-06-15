def matrix(n=2): 
    for i in range(n):
        print("* "*n)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    n = int(number)
    if n > 0 and n < 10:
        matrix(n) 
    else:
        print("Input Error!")  #有实参调用自定义函数

