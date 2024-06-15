def search(nums):
      for i in nums:
           if nums.ount(i)>len(nums)//2:
                return i   
           else:
                 return "False"





nums = eval(input())
y = search(nums)
print(y)


