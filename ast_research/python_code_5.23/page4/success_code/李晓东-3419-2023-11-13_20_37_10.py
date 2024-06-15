def calDegrees(nums):
    list = []
    for i in nums:
        a = nums.count(i)
        list.append(a)
    b = max(list)
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

