def search(nums):
    m=len(nums)/2
    s=0
    for i in range(0,len(nums)):
       f=nums.count([i])
       if  f>=m:
           s=m
           num=nums[i]
    if s is False:
        num=eval(False)
    return(num)





nums = eval(input())
y = search(nums)
print(y)


