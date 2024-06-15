def test(*para):
    while True:
        lst = list(*para)
        n = 1
        for i in lst:
            n *=i
        return n
    else:
    print("-1")

    

origin=input().split()
origin=[eval(x) for x in origin]
number=origin[0]  #获取参数个数
if number==0:
    result=test()
elif number==1:
    result=test(origin[1])
elif number==2:
    result=test(origin[1],origin[2])
elif number==3:
    result=test(origin[1],origin[2],origin[3])
print(result)

