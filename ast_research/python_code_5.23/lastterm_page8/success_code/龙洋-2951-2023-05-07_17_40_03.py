def matrix(n=2): 
    y="*"
    for x in rang(n-1):
     y=y+" *"
    for x in range(n):
     print(y)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

