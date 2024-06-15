def calDegrees(nums):
    x=[]
    m=1
    for i in nums:
        if i not in x:
            m=1
        else:
            m+=1
    return m



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

