
def calDegrees(nums):
    freq_dict = {}
    max_freq = 0
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
        max_freq = max(max_freq, freq_dict[num])
    return max_freq


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

