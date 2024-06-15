n=int(input())
nums=list(range(1,n+1))
a=nums[0]
nums.remove(a)
nums.append(a)
print(nums)
