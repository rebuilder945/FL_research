def calDegrees(nums):
    b=[]
    for i in nums:
        a=nums.count(i)
        b.append(a)
    return max(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

