def search(nums):
 nums = []
 for i in range(len(nums)):  
  if nums.count(nums[i])>1:
   b = nums[i]
 else:
   b = False 
 return(b)
 
      
      
 





nums = eval(input())
y = search(nums)
print(y)


