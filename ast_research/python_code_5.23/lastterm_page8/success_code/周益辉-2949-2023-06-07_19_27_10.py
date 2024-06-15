def test(*para):
    lst1=[para]
    if lst1==[]:
        return -1
    elif len(lst1)==1:
        return lst1[0]
    elif len(lst1)==2:
        return lst1[0]*lst[1]
    elif len(lst1)==2:
        return lst1[0]*lst[1]*lst[2]
    

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

