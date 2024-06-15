def test(*para):
    a=[*para]
    if len(a)==0:
       return -1
    elif len(a)==1 or 2 or 3:
       b=1
       for i in a:
          b*=i
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

