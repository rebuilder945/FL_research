def matrix(n=2): 
    a=''
    for i in range(n-1):
        a+='* '
    a+='*'
    for x in range(n):
        print(a)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    martrix(int(number))  #有实参调用自定义函数

