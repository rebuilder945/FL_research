def matrix(n=2): 
    n=int(n)
    lst=['*']*n
    for x in range(n):
        print(*lst,end="")
        print("\n")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

