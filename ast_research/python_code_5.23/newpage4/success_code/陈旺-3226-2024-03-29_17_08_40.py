def search(nums):
  c=[]
  for i in nums:
    if nums.count(i)>=(len(nums)/2):
         c.append(i)                   
    else:
        None
  if len(c)==len(nums):
      if nums[1:]==nums[:-1]:
         y=c[o]
      else:
        y="false"
  elif  len(c)==0:
     y="false"
  else:
     y=c[0]
  return(y)





nums = eval(input())
y = search(nums)
print(y)


