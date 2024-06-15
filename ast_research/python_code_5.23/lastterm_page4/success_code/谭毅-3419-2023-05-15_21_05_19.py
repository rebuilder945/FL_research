def calDegrees(nums):
    counts = {}
    max_count = 0
    max_num = 0
    positions = {}
    for i, num in enumerate(nums):
        if num not in counts:
            counts[num] = 1
            positions[num] = [i]
        else:
            counts[num] += 1
            positions[num].append(i)
        if counts[num] > max_count:
            max_count = counts[num]
            max_num = num
    degree = max_count
    return degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

