def cal_degrees(nums):
    freq_dict = {}
    
    # 统计各个元素的频率
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    max_freq = max(freq_dict.values()) # 找到频率的最大值
    
    return max_freq



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

