def calDegrees(nums):
    b=[]
    for i in nums:
        b.append(nums.count(i))
    return max(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

