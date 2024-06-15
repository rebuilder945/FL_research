def test(*para):
    c = 1
    x = 1
    for x in para:
        c = x*c
    if c!=0 and c!=1: 
        return c
    else:
        return -1 
    

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

