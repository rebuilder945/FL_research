nums=eval(input)
n=len(nums)
def search(nums):
      max=0
      for i in nums:
            if (max<nums.count(i)):
                max=nums.count(i)
                if max>n//2:
     return i
                else:
     return false
      
            
      






nums = eval(input())
y = search(nums)
print(y)


