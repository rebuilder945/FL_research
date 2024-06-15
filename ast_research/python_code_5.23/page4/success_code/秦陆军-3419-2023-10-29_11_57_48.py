def calDegrees(nums):
    # 创建一个字典来存储每个元素出现的频率
    freq_dict = {}
    max_freq = 0  # 用于记录最大频率

    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

        # 更新最大频率
        max_freq = max(max_freq, freq_dict[num])

    return max_freq


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

