def calDegrees(nums):
    b=[]
for i in range(len(nums)):
    d=nums[i]
    g=nums.count(d)
    b.append(g)
f=max(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

