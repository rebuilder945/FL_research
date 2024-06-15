def calDegrees(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    max_freq = max(freq.values())
    return max_freq



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

