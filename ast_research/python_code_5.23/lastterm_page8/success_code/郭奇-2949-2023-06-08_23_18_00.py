def test(*para):
    def product(*args):
        """
        计算任意个正整数的乘积
        :param args: 任意个正整数，可为0个、1个、2个或3个
        :return: 所有参数的乘积，如果实际参数个数为0，返回-1
        """
        if len(args) == 0:
            return -1
        result = 1
        for x in args:
            if x <= 0:
                return -1
            result *= x
        return result

    

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

