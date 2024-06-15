def calDegrees(lis):
    for i in lis:
        x=0 
        if  lis.count(i)>x:
            x=lis.count(i)
        else:
            return x



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

