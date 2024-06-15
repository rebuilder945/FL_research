def calDegrees(nums):
    frequency_dict={}
    max_frequency=0

    for x in nums:
        if x in frequency_dict:
            frequency_dict[item]+=1
        else:
            frequency_dict[item]=1

        if frequency_dict[item]>max_frequency:
            max_frequency=frequency_dict[item]
    return max_frequency


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

