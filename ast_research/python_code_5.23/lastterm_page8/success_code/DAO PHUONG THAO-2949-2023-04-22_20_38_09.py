def test(*para):
    def  test(*para):
        
        if len(para)==0: #如果参数长度为0，对应输入的的数的个数为0，则返回-1
            return -1
            
        #print("para",para)
        #其他情况遍历参数元组的每一项，然后逐一把他转换为整数，把他们相乘，然后返回即可
        result = 1
        for i in para:
            j = int(i)
            result*=j
            #print("j=",j,",result=",result)
        
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

