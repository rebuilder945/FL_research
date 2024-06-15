def calDegrees():
    nums=eval(input())
    for x in range(0,len(nums)):
        a=nums[x:x+1]
        b=nums.count(a)
    return max(b)

nums=eval(input())
d=calDegrees(nums)
print(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

