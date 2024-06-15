def calDegrees(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    return max(count_dict.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

