def matrix(n=2): 
    for x in list(range(len(data2))):
        data2[x] = data2[x][0:8]
        return data2
    for i in list(range(int(n))):
        for j in list(range(int(n))):
            print("*",end=" ")
            print("")

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(number)  #有实参调用自定义函数

