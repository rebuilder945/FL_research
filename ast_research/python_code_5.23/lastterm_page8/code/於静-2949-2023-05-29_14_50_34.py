def test(*para):
    if len(para)==0:
            return(-1)
        else:
            if len(para)==3:
                return para[2]
            elif len(para)==5:
                return para[2]*para[4]
            else:
                return para[2]*para[4]*para[6]
    

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

