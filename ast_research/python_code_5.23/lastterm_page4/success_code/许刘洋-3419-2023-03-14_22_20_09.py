def calDegrees(biao):
    for x in biao:
        y=biao.count(x)
        aaa=[]
        aaa.append(y)
        return max(aaa)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

