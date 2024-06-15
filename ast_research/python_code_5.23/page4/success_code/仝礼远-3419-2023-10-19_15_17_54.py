def calDegrees(nums):
    for x in nums:
        m=[]
        m.append(nums.count(x))
    return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

