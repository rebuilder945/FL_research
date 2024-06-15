def search(nums):
 nums = []
 for i in range(len(nums)):
  if count(nums[i])>len(nums)//2:
   b = nums[i]
 else:
   b = False 
 return(b)
 
      
      
 





nums = eval(input())
y = search(nums)
print(y)


