def calDegrees(nums):
    list = []
    list1 = []
    for i in nums:
        if not i in list:
            list.append(i)
    for i in list:
        list1.append(nums.count(i))
    return max(list1)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

