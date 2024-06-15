def calDegrees(nums):
    for i in nums:
        l = []
        a = nums.count(i)
        l.append(a)
        return max(l)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

