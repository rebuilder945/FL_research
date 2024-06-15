def search(nums):
    for x in nums:
         if x>0.5*len(nums):
             return x
         else:
             print('False')





nums = eval(input())
y = search(nums)
print(y)


