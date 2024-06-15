def calDegrees(nums):
    b = []
    for i in nums:
        c = int(nums.count(i))
        b.append(c)
    return max(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

