def calDegrees(nums):
    max=0
    L=len(nums)
    x = {}
    for i in range(0,L):
        if x[nums[i]] is None:
            x[nums[i]] = 1
        else:
            x[nums[i]] += 1
    for key,value in x.items():
        if value>max:
            max=value
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

