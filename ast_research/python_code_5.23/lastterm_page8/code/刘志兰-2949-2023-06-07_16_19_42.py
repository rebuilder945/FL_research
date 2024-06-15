def test(*para):
        if *para[0]!=0:
            if number=1:
                result=test(*para[0])
            elif  number==2:
                result=test(*para[0],*para[1])
            elif  number==3:
                result=test*para[0]*para,[1]*para,[2])
        else:
            result=-1
        return result
    

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

