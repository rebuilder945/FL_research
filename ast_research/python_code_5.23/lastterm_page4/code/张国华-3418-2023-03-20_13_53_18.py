nums.sort()
min_sum=0
maxsum(nums)=0
for i in range(0,len(nums),2):
    min_sum+=nums[i]
    maxsum(nums)+=nums[i+1]




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

