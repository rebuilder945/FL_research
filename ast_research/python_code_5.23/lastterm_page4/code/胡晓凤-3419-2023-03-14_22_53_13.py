nums={ }
for i in eavl(input())：
    if i not in nums:
        nums[i]=1
    else:
        nums[i]+=1
calDegrees=(max(nums.values()))
d=calDegrees(nums)
print(d)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

