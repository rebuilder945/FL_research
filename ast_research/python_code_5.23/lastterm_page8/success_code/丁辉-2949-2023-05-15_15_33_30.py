def test(*para):
    a=list(para)
    if a==[]:
        return -1
    else:
        a[0]=i1
        for i in a[1:]:
            i*=i1
            i1=i
        return i1
    

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

