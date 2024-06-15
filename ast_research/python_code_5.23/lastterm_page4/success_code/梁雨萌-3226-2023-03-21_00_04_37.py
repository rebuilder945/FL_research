def search(nums):
    m=len(nums)/2
    s=0
    for i in range(0,len(nums)):
       f=nums.count([i])
       if  f>=m:
           s=f
           y=nums[i]
    if s is False:
        y=eval(False)
    return(y)
nums  =  eval(input())





nums = eval(input())
y = search(nums)
print(y)


