def test(*para):
    
        a=0 
        b=1
        if len(list(*para))==0:
            return -1
        else:
            for i in range(len(list(*para))):
                a=list(*para[i])
                b=b*a
            return int(b)

    

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

