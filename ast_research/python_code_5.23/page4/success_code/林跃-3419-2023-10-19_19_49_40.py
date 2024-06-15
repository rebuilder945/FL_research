def calDegrees(nums):
    for i in nums:
        m=[]
        m.append(nums.count(i))
    return max(m)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

