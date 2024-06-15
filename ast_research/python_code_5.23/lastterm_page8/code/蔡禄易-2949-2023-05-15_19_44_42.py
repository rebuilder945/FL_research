def test(*para):
    if *para == 0:
        return -1
    elif *para == (origin[1]) :
        return origin[1]
    elif *para == (origin[1],origin[2]):
        a = int(origin[1])*int(origin[2])
        return a
    elif *para == (origin[1],origin[2],origin[3]):
        b = int(origin[1]*origin[2]*origin[3])
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

