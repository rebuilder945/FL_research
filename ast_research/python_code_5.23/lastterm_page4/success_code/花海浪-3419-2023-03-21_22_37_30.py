def calDegrees(nums):
    b1=[]
    for x in nums:
        n=nums.count(x)
        if n not in b1:
            b1.append(n)
    return nums==b1


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

