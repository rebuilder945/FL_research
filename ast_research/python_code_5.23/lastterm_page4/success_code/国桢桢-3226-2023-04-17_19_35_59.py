def search(nums):
 nums = []
 for i in range(len(nums)):  
  if nums.count(nums[i])>len(nums)//2:
    y = nums[i]
  else:
    y = False 





nums = eval(input())
y = search(nums)
print(y)


