def test(*para):
    lst=list(*para)
        if list[0]==0:
            return(-1)
        else:
            if len(*para)==3:
                x=list[2]
            elif len(*para)==5:
                x=list[2]*list[4]
            else:
                x=list[2]*list[4]*list[6]
            return x
    

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

