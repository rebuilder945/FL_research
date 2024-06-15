def calDegrees(nums):
    for i in range(len(nums)):
        n=0
        max=0
        p=nums.count('nums[n]')
        if max<p:
            max=p
        n+=1
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

