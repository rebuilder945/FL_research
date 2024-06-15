def calDegrees(nums):
    count = {}
    max_degree = 0
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        max_degree = max(max_degree, count[num])
    return max_degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

