def test(*para):
    n=len(para)
    if n==0:
        return -1
    else:
        para=list(para)
        for i in para:
            if i.isdigit() and i>0:
                continue
            else:
                remove(i)
        n=1
        for m in para:
            n=n*m
        return n
    

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

