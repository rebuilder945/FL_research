def search(nums):
      n=len(nums)
      for x in nums:
            if nums.count(x)>n//2:
                z=x
            else:
                   z="False"
return z





nums = eval(input())
y = search(nums)
print(y)


