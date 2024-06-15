def search(nums):
      nums.sort(reverse=True)
      max=0
      now=1
      ans=1
      a=len(lst)-1
      for x in range(a):
           before=nums[x]
           after=nums[x+1]
           if after==before:
                ans=ans+1
           else:
                ans=1
           if ans>len(nums)//2:
                return(nums[x])
           return False





nums = eval(input())
y = search(nums)
print(y)


