nums=eval(input())
nums.sort()
m=0
for i in range(len(nums)):
    m+=nums[i]*10**i
print(m)
