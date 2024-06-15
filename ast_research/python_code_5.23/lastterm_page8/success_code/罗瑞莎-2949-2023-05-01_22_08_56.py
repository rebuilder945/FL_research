def test(*para):
    lst = list(*para)
    n = 1
    if len(lst) == 0:
        print("-1")
    elif len(lst) > 0:
        for i in lst:
            n *=i
        print(n)

    

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

