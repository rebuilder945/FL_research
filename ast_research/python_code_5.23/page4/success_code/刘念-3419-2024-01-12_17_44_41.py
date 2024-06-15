def calDegrees(nums):
    freq_dict = {}
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    max_freq = max(freq_dict.values())
    return max_freq
    
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

