def search(nums):
   a = len(nums)//2
   for y in nums:
    if nums.count(y)>a:
      return y
    else :
      return "False"
      return 





nums = eval(input())
y = search(nums)
print(y)


