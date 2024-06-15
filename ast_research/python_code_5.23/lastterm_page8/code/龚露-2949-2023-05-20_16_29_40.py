def test(*para):
    if *para==" ":
        return -1
    if *para==1:
        return origin[1]
    if *para==2:
        return origin[1]*origin[2]
    if *para==3:
        return origin[1]*origin[2]*origin[3]
    

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

