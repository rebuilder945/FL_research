def calDegrees(nums):
    m=[]
    for x in nums：
        n=nums.count(x)
        if n not in m:
            m.append(n)
    return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

