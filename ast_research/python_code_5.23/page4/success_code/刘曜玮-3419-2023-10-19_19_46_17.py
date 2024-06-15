def calDegrees(nums):
    list =[]
    for x in nums:
        a=nums.count(x)
        list.append(a)
    return max(list)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

