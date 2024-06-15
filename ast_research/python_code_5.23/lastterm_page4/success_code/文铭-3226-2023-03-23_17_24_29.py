def search(nums):
      for x in nums:
             if nums.count(x)>=len(nums)//2:
                  k = x
             else :
                  k = "False"
      return k





nums = eval(input())
y = search(nums)
print(y)


