def matrix(n=2): 
    for i range(n):
        print('"* "*n')


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n)  #有实参调用自定义函数

