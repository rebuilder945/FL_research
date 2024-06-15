def test(*para):
    l=list(*para)
    if len(l)==0:
        return -1
    elif l[0]==1:
        sum1=l[1]
        return sum1
    elif l[0]==2:
        sum2=l[1]*l[2]
        return sum2
    elif l[0]==3:
        sum3=l[1]*l[2]*l[3]
        return sum3
    

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

