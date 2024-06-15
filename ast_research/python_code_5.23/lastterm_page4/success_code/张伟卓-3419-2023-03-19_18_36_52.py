def calDegrees(nums):
    num_dict = {}
    max_frequency = 0
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
        max_frequency = max(max_frequency, num_dict[num])
    return max_frequency


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

