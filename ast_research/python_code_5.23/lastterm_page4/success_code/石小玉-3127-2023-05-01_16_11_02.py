iA=int(input())
nums=range(1,iA+1,1)
a=nums[0]
nums.remove(a)
nums.append(a)
print(nums)


