def calDegrees(nums):
    counts = Counter(nums)
    max_count = max(counts.values())
    max_nums = [num for num, count in counts.items() if count == max_count]
    if len(max_nums) == 1:
        max_num = max_nums[0]
        degree = max_count
    else:
        degree = len(nums)
    return degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

