def search(nums):
    for x in nums:
         if  nums.count(x)>0.5*len(nums):
             return x
         else:
             return False





nums = eval(input())
y = search(nums)
print(y)


