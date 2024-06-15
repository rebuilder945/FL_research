def calDegrees(nums):
    b=[]
    for i in nums:
        b=0
        for a in nums:
            if i==a:
                b=b+1
        op.append(b)
    m=max(op)
    return m



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

