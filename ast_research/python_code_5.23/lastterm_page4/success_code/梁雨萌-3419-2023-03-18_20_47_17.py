def calDegrees(nums):
    d=0
    for i in range(len(nums)):
        sum=nums.count(i)
        if sum>=d :
            d=sum
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

