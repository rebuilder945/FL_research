def test(*para):
    def product(*args):
        if len(args) == 0:
            return -1
        elif len(args)==1:
            return args[1]
        elif len(args)==2:
            return args[1]*args[2]
        elif len(args)==3:
            return args[1]*args[2]*args[3]
        
    

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

