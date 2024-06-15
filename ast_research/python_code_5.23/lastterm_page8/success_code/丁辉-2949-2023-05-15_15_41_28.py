def test(*para):
    a=list(para)
    if len(a)==0:
        return -1
    if len(a)==1:
        return a[0]
    if len(a)>1:
        i1=a[0]
        for i in a[1:]:
            i*=i1
            i1=i
        return i1
        
    

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

