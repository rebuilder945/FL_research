def matrix(n=2): 
            a=["*"]
            for x in range(n-1):
                a.append('*')
            print(a),)

number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(eval(number))  #有实参调用自定义函数

