def test(*para):
    a=list(*para)
    b=len(a)
    c=1
    if b==0:
      return -1
    else:  
      for i in a:
        c*=i
      return c
    

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

