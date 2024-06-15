def calDegrees(nums):
    b=[]
    a=max(nums)
    for i in nums:
        if i==a:
            b.append(i)
        else:
            continue
    return len(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

