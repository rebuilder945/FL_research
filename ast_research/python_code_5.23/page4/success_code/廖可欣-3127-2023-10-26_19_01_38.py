n = int(input())
nums = [x for x in range(1,n+1)]
k = nums[0]
nums.remove(k)
nums.append(k)
print(nums)
