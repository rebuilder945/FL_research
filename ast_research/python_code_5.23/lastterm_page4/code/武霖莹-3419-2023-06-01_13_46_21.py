lst1 = []
    for x in nums:
        lst1.append(nums.count(x))
    n = max(lst1)
    return n


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

