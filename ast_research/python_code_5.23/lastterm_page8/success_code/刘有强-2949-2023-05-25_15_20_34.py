def test(*para):
        b=list(para)
        if number == 0:
            return -1
        elif number==1:
            return b[-1]
        elif number==2:
            return b[-2]*b[-1]
        elif number==3:
            return b[-3]*b[-2]*b[-1]
    

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

