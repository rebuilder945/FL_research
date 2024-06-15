def search(nums):
      a=max(nums,key=nums.count)
      if nums.count(a)>len(nums)/2:
          return(a)
      else:
          return('False')






nums = eval(input())
y = search(nums)
print(y)


