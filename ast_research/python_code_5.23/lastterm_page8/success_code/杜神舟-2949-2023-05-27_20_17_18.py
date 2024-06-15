def test(*para):
        if para==():
            return -1
        else:
            if len(para)==1:
                b=list(para)[0]
            elif len(para)==2:
                b=list(para)[0]*list(para)[1]
            else:
                b=list(para)[0]*list(para)[1]*list(para)[2]
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

