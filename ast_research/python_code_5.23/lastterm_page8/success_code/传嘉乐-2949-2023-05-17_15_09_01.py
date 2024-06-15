def test(*para):
        print(*para)
        if para=='':
            return -1
        else:
            b=1
            a=para.split()
            for x in a:
                b=b*x
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

