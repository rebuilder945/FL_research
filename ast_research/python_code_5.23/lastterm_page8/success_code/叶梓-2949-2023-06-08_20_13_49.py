def test(*para):
    nums=1
    if len(para)==0:
        nums=-1
    else:
        for i in range(len(para)):
            nums=nums*para[i]
    return nums
    

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

