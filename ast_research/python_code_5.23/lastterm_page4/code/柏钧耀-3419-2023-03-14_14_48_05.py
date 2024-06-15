def calDegrees(nums):
    freq = {}  
    for num in nums:
    freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())
    return max_freq 


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

