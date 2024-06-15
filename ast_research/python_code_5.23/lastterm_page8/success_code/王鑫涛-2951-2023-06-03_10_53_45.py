def matrix(n=2): 
    c=[]
    b=[]
    for i in range(int(n)):
        b.append('*')
    for r in range(int(n)):
        c.append(b)
    for p in c:
        for q in p:
            print(q,end='')
        print('')


number=input()
if number=="default":
    matrix() #无实参调用自定义函数
else:
    matrix(n=number)  #有实参调用自定义函数

