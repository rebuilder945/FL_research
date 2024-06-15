def calDegrees(nums):
    z=[]
    for i in nums:
        b=nums. count(i)
        z.append(b)
    return max(z)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

