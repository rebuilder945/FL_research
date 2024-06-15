def search(nums):
      for i in nums:
           if i>len(nums):
                return i   
           else:
                return "False"





nums = eval(input())
y = search(nums)
print(y)


