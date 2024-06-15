def matrix(n=2): 
    for i in range(n):
        b.append('*')
    for r in range(n):
        c.append(b)
    for p in c:
        for q in b:
            print(q,end='')


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

