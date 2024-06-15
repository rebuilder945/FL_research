def find_degree(nums):
    freq_dict = {}
    max_freq = 0
    
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
        
        max_freq = max(max_freq, freq_dict[num])
    
    return max_freq



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

