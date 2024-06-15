def calDegrees(nums):
a = [ ]
for i in nums:
    i_count = nums.count(i)
    a.append(i_count)
c= max(a)
    return c



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

