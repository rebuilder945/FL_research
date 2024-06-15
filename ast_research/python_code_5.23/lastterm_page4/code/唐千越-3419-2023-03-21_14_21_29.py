pl=[]
for x in nums:
    k=nums.count(x)
    pl.append(k)
c=max(pl)
return c


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

