def test(*para):
    if *para=''
        return -1
    elif *para.count==1
        return *para
    elif *para.count==2
        return *para[0]**para[1]
    elif *para.count==3
        return *para[0]**para[1]**para[2]
        
    

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

