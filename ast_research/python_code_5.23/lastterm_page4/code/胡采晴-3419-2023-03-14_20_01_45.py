def calDegrees(nums):
a=[]
for x in nums:
c=nums.count(x)
a.append(c)
d=max(a）
return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

