def test(*para):
    if True:
        ls=list(*para.split(" "))
        s=1
        for i in ls:
             i=int(i)
             s=s*i
        return s
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

