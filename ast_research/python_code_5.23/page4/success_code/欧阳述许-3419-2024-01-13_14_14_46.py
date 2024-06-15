def calDegrees(nums):
    d=[nums.count(x) for x in list(nums)]
    return max(d)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

