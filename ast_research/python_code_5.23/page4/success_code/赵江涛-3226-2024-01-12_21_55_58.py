def search(nums):
 n = 0
 for num in nums:
  if nums.count(num) > (len(nums)//2):
   n = 1
   print(num)






nums = eval(input())
y = search(nums)
print(y)


