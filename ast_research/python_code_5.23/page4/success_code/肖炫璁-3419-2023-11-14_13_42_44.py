def calDegrees(nums):    
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_frequency = max(frequency.values())

    return max_frequency



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

