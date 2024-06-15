def matrix(n=2): 
        ls = []
        for i in range(n):
            ls.append('*')
        a = ' '.join(ls)
        for i in range(n):
            print(a)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

