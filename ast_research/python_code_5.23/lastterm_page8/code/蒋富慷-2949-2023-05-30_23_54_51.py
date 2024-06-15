def test(*para):
    b = 1
    if para == :
        return (-1)
    else:
        a = list(para)
        for x in range(len(a)):
            b = b*a[x]
        return b
    

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

