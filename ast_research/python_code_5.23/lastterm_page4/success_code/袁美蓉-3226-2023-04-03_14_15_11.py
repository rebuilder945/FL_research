def search(nums):
 for y in nums:
    if nums.count(y)>len(nums)//2:
        return y
    else:
          return("False") 





nums = eval(input())
y = search(nums)
print(y)


