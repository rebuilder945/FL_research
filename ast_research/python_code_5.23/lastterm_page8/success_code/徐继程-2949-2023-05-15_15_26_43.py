def test(*para):
        end=1
        lst=[]
        for x in para:
            lst.append(x)
        if len(lst)<=1:
            return -1
        else:
            for x in para:
                end*=x
        return end
    

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

